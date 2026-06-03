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

Internal links between pages are written **relative** (e.g. `../skills/discovery/`) so they remain
correct under the project base path and would also survive a move to a custom domain.
