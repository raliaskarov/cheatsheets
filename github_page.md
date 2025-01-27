# Deploy to github pages

## React
Install
```
npm install gh-pages --save-dev
```
Add before "build": "vite build" in package.json:
```
"predeploy": "npm run build",
"deploy": "gh-pages -d dist",
```
in the vite.config.js file add this line before plugins: [react()]
```
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: "react_tutorial_learning_react", // add this line
  plugins: [react()],
})

```
deploy
```
npm run deploy
```
In github repo visit settings, then pages
