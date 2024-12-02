# Contribution Guide
This is pretty much a tutorial on setting up your local development environment.

1. Get `node` and `npm`
2. Install Wrangler: `npm i wrangler`
3. Clone the repository (if you haven't already done so)
4. cd to the root of the repository (not `elSSGin` or `site`)
5. `npm wrangler pages dev`
6. Profit

Make sure to only use Wrangler, which is pretty much a local Cloudflare Pages, so that Pages redirects and Workers work correctly.