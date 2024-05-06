## Theme
[LoveIt Theme | Hugo](https://github.com/dillonzq/LoveIt)

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
### Error Handle
`failed to extract shortcode: template for shortcode "admonition" not found`

[Failed to Extract Shortcode:template for Shortcode Admonition Not Found](https://cloud.tencent.com/developer/article/2171926)
```cmd
1、下载安装hugo_extended版本

2、初始化submodule

git submodule update --init --recursive
```