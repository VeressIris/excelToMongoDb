# Table to MongoDB converter

A web app that converts either a Google Sheets table or a Microsoft Excel table into a MongoDB database.

See it in action at: https://tabletomongodb.vercel.app

<img src="https://github.com/user-attachments/assets/f58ec10a-e66f-48b3-894b-1fa91859fa65" width="800px" alt="Image 1">
<img src="https://github.com/user-attachments/assets/81f22309-8670-4860-9a05-d91f8ed6f725" width="800px" alt="Image 2">

# Technologies

- Sveltekit
- Tailwindcss
- Flask

# Building yourself

Here are the instructions for setting up a svelte project:

## Setting up Svelte

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

### Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

### Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

### Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## Tailwindcss

The instructions for setting up Tailwindcss with Sveltekit can be found here https://tailwindcss.com/docs/guides/sveltekit

## Setting up Flask

Run this command to build the app before each deploy.

```bash
pip install -r requirements.txt
```

Run this command to run the app locally.

```bash
flask --app main.py run
```

## Building Flask for production

Run this command to start the app with each deploy.

```bash
gunicorn main:app
```
