# Online Writing — documentation site

The documentation site for the [Online Writing](https://github.com/DonHeidi/online-writing-skills)
plugin, built with [Astro Starlight](https://starlight.astro.build/) and deployed to GitHub Pages at
<https://donheidi.github.io/online-writing-skills/>.

## Local development

```sh
cd site
npm install
npm run dev      # local dev server at http://localhost:4321/online-writing-skills/
npm run build    # production build to ./dist
npm run preview  # preview the production build
```

## Structure

- `src/content/docs/` — the documentation pages (Markdown / MDX)
  - `index.mdx` — landing page
  - `guides/` — installation, getting started, configuration
  - `skills/` — skill reference, grouped by stage
- `astro.config.mjs` — site URL, base path (`/online-writing-skills`), and sidebar

## Deployment

Pushes to `main` that touch `site/**` trigger the `.github/workflows/deploy-docs.yml` workflow, which
builds the site and publishes it to GitHub Pages. The repository's **Settings → Pages → Source** must
be set to **GitHub Actions**.

Internal links between pages are written as **absolute, base-prefixed** paths (e.g.
`/online-writing-skills/skills/discovery/`). Astro does not auto-prefix the configured `base` to
authored links, and relative links break on the splash page (served at the bare base without a
trailing slash) — so absolute base-prefixed links are used for correctness in both dev and
production. If the `base` ever changes (e.g. a move to a custom domain at the root), update the
`/online-writing-skills` prefix across `src/content/docs/`.
