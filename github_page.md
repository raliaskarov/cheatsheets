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
  base: "react_tutorial_learning_react", // add this line
```
deploy
```
npm run deploy
```
In github repo visit settings, then pages
