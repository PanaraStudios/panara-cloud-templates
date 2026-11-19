# Panara Cloud templates

One-click templates for [Panara Cloud](https://github.com/PanaraStudios/panara-cloud), the
open-source, self-hosted platform for deploying apps, Docker Compose stacks and databases to
your own servers.

The panel reads this catalog from
`https://panarastudios.github.io/panara-cloud-templates`:

- `meta.json`: every template's name, version, description, logo, links and tags.
- `blueprints/<id>/docker-compose.yml`, `template.toml` and the logo.

Point a Panara Cloud instance at a different catalog in **Settings → General → Templates**, or
with the `TEMPLATES_BASE_URL` environment variable.

## Adding a template

1. Create `blueprints/<id>/` with `docker-compose.yml`, `template.toml`, `meta.json` and a logo.
   `meta.json` holds `id` (same as the folder), `name`, `version`, `description`, `logo`,
   `links` (`github`, `website`, `docs`) and `tags`.
2. Services join the shared `panara-cloud-network` only when they need it; domains are set in
   `template.toml`.
3. Run `python3 scripts/build-meta.py` and commit the updated `meta.json`.

## License

MIT. See [LICENSE](LICENSE).
