## Codespaces Usage
1. install **hugo-installer**

    `npm install hugo-installer --save-dev`
  
2. Configure hugo version (required) in **package.json**

    ```json
    {
      "scripts": {
        "postinstall": "hugo-installer --version 0.121.1 --extended"
      }
    }
    ```

3. `npm run postinstall` to install Hugo
4. `bin/hugo/hugo server` to run **hugo server**
