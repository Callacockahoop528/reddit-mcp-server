# Contributing to Reddit MCP Server

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Getting Started

```bash
# Clone the repository
git clone https://github.com/eliasbiondo/reddit-mcp-server.git
cd reddit-mcp-server

# Install dependencies (including dev)
uv sync

# Run the server
uv run reddit-mcp-server --help
```

## Architecture

This project follows **hexagonal architecture** (ports & adapters). Please maintain this separation when contributing:

### Layers

1. **Domain** (`domain/`) — Pure business logic, exceptions, value objects. No framework imports.
2. **Ports** (`ports/`) — Abstract interfaces (ABCs) defining contracts.
3. **Application** (`application/`) — Use cases that orchestrate business logic via ports.
4. **Adapters** — Concrete implementations:
   - **Inbound** (`adapters/inbound/`) — Entry points: CLI, MCP server, MCP tools.
   - **Outbound** (`adapters/outbound/`) — Infrastructure: redd client, config loading.
5. **Container** (`container.py`) — Dependency injection composition root.

### Rules

- **Domain and Application layers must never import from Adapters.**
- **Application layer depends only on Ports**, never on concrete implementations.
- **Only `container.py` imports concrete adapter classes** to wire everything together.
- **MCP tools import only from Application (use cases) and Inbound adapters** (serialization, error mapping).

## Code Style

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
# Lint
uv run ruff check src/

# Format
uv run ruff format src/

# Fix auto-fixable issues
uv run ruff check --fix src/
```

### Conventions

- Line length: 100 characters
- Target Python version: 3.12
- Use type hints everywhere
- Use `frozen=True` dataclasses for value objects
- Use `async/await` in ports and adapters (redd uses async client)

## Testing

```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=reddit_mcp_server
```

## Adding a New Tool

1. **Add method to `RedditPort`** (`ports/reddit.py`) if the underlying redd client supports it.
2. **Implement in `ReddClientAdapter`** (`adapters/outbound/redd_client.py`).
3. **Create a use case** in `application/`.
4. **Register in Container** (`container.py`).
5. **Create MCP tool** in `adapters/inbound/mcp_tools/`.
6. **Register in `mcp_server.py`** (`adapters/inbound/mcp_server.py`).

## Pull Request Process

1. Fork the repository and create your branch from `main`.
2. Follow the architecture guidelines above.
3. Add tests for new functionality.
4. Run linting and formatting before submitting.
5. Update the README if you're adding new tools or configuration options.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
