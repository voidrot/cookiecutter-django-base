from pathlib import Path

def is_docker():
    """
    Check if the current environment is running inside a Docker container.
    """
    cgroup = Path('/proc/self/cgroup')
    return Path('/.dockerenv').is_file() or cgroup.is_file() and 'docker' in cgroup.read_text()
