Deployment notes for Vercel

1) Do NOT commit SECRET_KEY. Set it in Vercel project settings:
   - Vercel Dashboard → Project → Settings → Environment Variables
   - Add SECRET_KEY with a strong random value (Production scope)

2) DEBUG is set to "False" by default in vercel.json. If you need debugging, set DEBUG to "True" in Vercel env (not in source).

3) Requirements
   - requirements.txt has the core packages. Vercel will install these automatically during build.

4) Static files
   - The project uses whitenoise. Ensure collectstatic runs if needed. On Vercel you can run collectstatic during the build step by adding a Build Command in the Vercel UI such as:
     python manage.py collectstatic --noinput
   - Alternatively run collectstatic elsewhere and commit static files to a suitable location.

5) Migrations
   - Vercel deployments are serverless and not intended to run long-running DB migrations automatically.
   - Run migrations separately (from your development machine, CI, or a small ephemeral server) against your production database:
     python manage.py migrate

6) Other environment variables
   - If you use a different DB, email provider, or third-party services, set those credentials in Vercel Environment Variables as well.

7) After setting env vars
   - Push changes to your git branch, then trigger a redeploy on Vercel (or push to the branch Vercel watches).
   - Check Vercel build and function logs to confirm the function starts cleanly.

If you want, I can also:
 - Add a simple build command to vercel.json (runs collectstatic) instead of using the UI
 - Create a small script / GitHub Action to run migrations
Tell me which of those (if any) to add next.