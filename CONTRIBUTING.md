# Contribution Guide
## Wrangler environment setup

1. Get `node` and `npm`
2. Clone the repository (if you haven't already done so)
3. cd to the root of the repository (not `elSSGin` or `site`)
4. Install Wrangler: `npm i wrangler`
5. `npx wrangler pages dev`
6. Profit

Make sure to only use Wrangler, which is pretty much a local Cloudflare Pages, so that Pages redirects and Workers work correctly.

## Editing data
Department and club data is stored in `elSSGin/pods`; every JSON data file is called a "pod".

Before you edit, set the schemas (`elSSGin/pods/schemas`) in your IDE or editor. **Don't break the site. Don't edit without the schema.**

## Handling edit requests
1. If you don't have access to the forms, ask in the Computer Programming Club team on Teams for access to form data
2. Wait for requests
   - You'll be emailed when a new request is submitted
3. Read the request
   - Requests sent through the staff & students form should be more trusted, as it requires SD36 login
   - First submitted, first handled
   - **Do not delete old requests. They are to be kept for tracking purposes.**
4. Respond
   - Staff & students form: download as Excel spreadsheet, and find the email. If requester chose Teams, start a chat and entet the email address as the name.
   - Parents & visitors form: Email is in the form as a field
   - Use the templates in the wiki
5. Implement
   - Edit the files
   - Increase the edit request counter
   - Use the following commit message:
     - Implement edit request #_{{ ID }}_
   - **Do not include name, email, or any other info other than ID**