# Base image
FROM python:3.12-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Ensuring the libraries installed by the user are added to the PATH
ENV PATH="/home/user/.local/bin:$PATH"

# Create a new user according to HF standards
RUN useradd -m -u 1000 user
USER user
WORKDIR /home/user/app

# Copy requirements and install
# We install as user 1000
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt \
    && pip install --user supervisor

# Copy project files with user ownership
COPY --chown=user . .

# Supervisord config
# Put it in a place that the user can access
COPY --chown=user supervisord.conf /home/user/app/supervisord.conf

# Expose ports
EXPOSE 8000 7860

# Run supervisord using the user's local path
CMD ["python3", "-m", "supervisor.supervisord", "-c", "/home/user/app/supervisord.conf"]