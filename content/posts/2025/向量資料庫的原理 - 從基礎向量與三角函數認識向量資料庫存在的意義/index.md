---
title: "TypeScript and Vue"
date: 2024-12-26T00:00:00+08:00
lastmod: 2024-12-26T00:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://hsiang.eu.org/"
images: ["posts/2024/typescript-and-vue/type-warning.png"]
featuredimage: type-warning.png
tags: ["Typescript", "Vue", "Vuejs", "Vue 3", "JavaScript"]
toc:
  enable: true
lightgallery: true
zhtw: true
---
## 什麼是向量資料庫
向量資料庫是一種專門用來存儲和管理向量嵌入（Vector Embedding）的資料庫。向量嵌入是數據對象的數字表示，這些數據對象可以是圖片、文字或感測器數據等非結構化或半結構化數據。

向量資料庫的主要功能包括：
-   **索引和搜尋**：利用高維向量來組織數據，並使用算法對向量嵌入進行索引和查詢。常見的算法有哈希（Hash）、量化（Quantization）和基於圖的搜尋。
-   **相似度度量**：向量資料庫依賴數學方法來確定向量之間的相似度，例如餘弦相似度、歐氏距離和點積相似度。
-   **元數據管理**（Metadata Management）：除了向量索引外，向量資料庫還會為數據對象的元數據建立索引，支持元數據的儲存和篩選。

向量資料庫在機器學習和人工智慧領域中非常重要，因為它們能夠高效地處理和管理大量的非結構化數據，並支持相似度搜尋和模式識別。

## 如何計算資料點之間的距離
計算資料點之間的距離可以使用不同的方法，取決於資料點的類型和應用場景。以下是一些常見的方法：

歐幾里得距離

歐幾里得距離是最常見的距離計算方法，適用於平面幾何中的兩點。假設兩點的座標分別為 \((x_1, y_1)\) 和 \((x_2, y_2)\)，則它們之間的距離 \(d\) 可以用以下公式計算：

\[ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]

例如，已知點 \(A (2, 3)\) 和點 \(B (8, 7)\)，求這兩點之間的距離：

\[ d = \sqrt{(8 - 2)^2 + (7 - 3)^2} = \sqrt{36 + 16} = \sqrt{52} \approx 7.21 \]

曼哈頓距離

曼哈頓距離（也稱為城市街區距離）是另一種常見的距離計算方法，適用於網格狀結構中的兩點。假設兩點的座標分別為 \((x_1, y_1)\) 和 \((x_2, y_2)\)，則它們之間的距離 \(d\) 可以用以下公式計算：

\[ d = |x_2 - x_1| + |y_2 - y_1| \]

餘弦相似度

餘弦相似度通常用於計算高維向量之間的相似度。假設兩個向量 \(A\) 和 \(B\) 的分量分別為 \(A = (a_1, a_2, \ldots, a_n)\) 和 \(B = (b_1, b_2, \ldots, b_n)\)，則它們之間的餘弦相似度 \(cos(\theta)\) 可以用以下公式計算：

\[ cos(\theta) = \frac{A \cdot B}{||A|| \cdot ||B||} = \frac{\sum_{i=1}^{n} a_i b_i}{\sqrt{\sum_{i=1}^{n} a_i^2} \cdot \sqrt{\sum_{i=1}^{n} b_i^2}} \]

這些方法在不同的應用場景中有不同的優勢和適用性。



## 簡介
**Vue.js** 可以使用 **JavaScript（JS）** 和 **TypeScript（TS）**。**TypeScript** 是 **JavaScript** 的超集，增加了靜態類型檢查和其他高級功能。使用 **TypeScript** 可以提高代碼的可讀性和可維護性，並減少運行時錯誤。
-  **TypeScript**
    *   **Static Type Checking**: TypeScript allows you to check for type errors at compile time, which helps in early detection and fixing of errors.
    *   **Interfaces and Classes**: TypeScript supports interfaces and classes, making the code more structured and scalable.
    *   **Modules and Namespaces**: TypeScript supports modules and namespaces, which help in organizing code and avoiding naming conflicts.

   TL;DR
    1.   `.ts` 是 `.js` 的 superset 加上 static types _(like `.scss` to `.css`)_
    2.   Compiles to plain JavaScript, which can run anywhere **JavaScript** runs

-  **Vue.js**
   _(**JavaScript** 現代前端框架之一 )_
    - 前端框架包含先寫好的 ( 常見、常用的功能模組 ) `html`, `css`, `js` 供開發者隨時快速調用
    - 大量可重用組件 _(microservices)_

### 從安裝到開始
**TypeScript**
```bash
npx tsc hello.ts
node hello.js
```
**Vue**
```bash
npm install -g @vue/cli
vue create my-vue-app
cd my-vue-app
npm run serve # Open your browser and navigate to `http://localhost:8080`
```
### 常見的結構
#### Vue.js
    /src
      /assets
      /components
      /router
      /store
      /views
      App.vue
      main.js
    

*   `/src`：主要的源代碼目錄。
*   `/assets`：靜態資源，如圖片、樣式等。
*   `/components`：Vue 組件。
*   `/router`：路由配置。
*   `/store`：狀態管理（如 Vuex）。
*   `/views`：視圖組件。
*   `App.vue`：主應用組件。
*   `main.js`：應用入口文件。

#### React
    /src
      /assets
      /components
      /containers
      /redux
      /utils
      App.js
      index.js
    

*   `/src`：主要的源代碼目錄。
*   `/assets`：靜態資源。
*   `/components`：無狀態的展示組件。
*   `/containers`：有狀態的容器組件。
*   `/redux`：Redux 狀態管理。
*   `/utils`：工具函數。
*   `App.js`：主應用組件。
*   `index.js`：應用入口文件。

#### Angular
    /src
      /app
        /components
        /services
        /models
        /modules
        /shared
        app.component.ts
        app.module.ts
      /assets
      /environments
      main.ts
      index.html
    

*   `/src`：主要的源代碼目錄。
*   `/app`：應用的主要代碼。
    *   `/components`：Angular 組件。
    *   `/services`：服務。
    *   `/models`：數據模型。
    *   `/modules`：模塊。
    *   `/shared`：共享組件和服務。
    *   `app.component.ts`：主應用組件。
    *   `app.module.ts`：主應用模塊。
*   `/assets`：靜態資源。
*   `/environments`：環境配置。
*   `main.ts`：應用入口文件。
*   `index.html`：主 HTML 文件。
## 範例
### 基礎 Types 與 Interfaces
```ts
interface User {
  name: string;
  age: number;
}
```
#### 創建物件
創建 **Objects** that conform to the `User` **Interface**
```ts
const user1: User = {
  name: 'Alice',
  age: 30
}

const user2: User = {
  name: 'Bob',
  age: 25
}
```
#### 功能呼叫
Using the **Interface** with **Functions**
```ts
function greet(user: User): string {
  return `Hello, ${user.name}! You are ${user.age} year old.`;
}

console.log(greet(user1)); // Output: Hello, Alice! You are 30 years old.
console.log(greet(user2)); // Output: Hello, Bob! You are 25 years old.
```
#### 使用 Interfaces 的好處
> ( 可以在 `compiletime` 就找到錯誤，不必等到 `runtime`)

_確保程式功能得以繼承或指定輸入結構_

案例一
```ts
const user3: User = {
  name: 'Charlie'
  // Error: Property 'age' is missing in type '{ name: string; }' but required in type 'User'.
};
```

案例二
```ts
console.log(greet({ name: 'Dave' }));
// Error: Argument of type '{ name: string; }' is not assignable to parameter of type 'User'.
// Property 'age' is missing in type '{ name: string; }' but required in type 'User'.
```

##### TypeScript 在除錯上更具優勢
JavaScript 錯誤範例: `runtime error`
```js
function greeting(name) {
    return 'Hello, ' + name.toUpperCase() + '!';
}
console.log(greeting(123));

// TypeError: name.toUpperCase is not a function
// 實際上在這個案例中，我們期待看到的錯誤應該是 smth like... TypeError: input @name is not the correct type
```
TypeScript 錯誤範例: `compiletime error`
```ts
function greeting1(name: string) {
    return 'Hello, ' + name.toUpperCase() + '!';
}
console.log(greeting1(456));
// Argument of type 'number' is not assignable to parameter of type 'string'.ts(2345)
```
甚至在 **IDE** 上開發時就能先看到提醒 **(未指定 `types` 時)**
![type-warning.png](type-warning.png "type-warning.png")

指定 `types` 後，在編譯前 **IDE** 上也會先出現錯誤
![type-error.png](type-error.png "type-error.png")

### 基礎 Vue 概念
Use Vue directly from a CDN via a script tag `<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>`:
```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<div id="app">{{ message }}</div>

<script>
  const { createApp, ref } = Vue

  createApp({
    setup() {
      const message = ref('Hello vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>
```
#### ES Module
```html
<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    setup() {
      const message = ref('Hello Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>
```
We can teach the browser where to locate the `vue` import by using [Import Maps](https://caniuse.com/import-maps):
```html
<script type="importmap">
  {
    "imports": {
      "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
    }
  }
</script>

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp, ref } from 'vue'

  createApp({
    setup() {
      const message = ref('Hello Vue!')
      return {
        message
      }
    }
  }).mount('#app')
</script>
```
#### Single-File Components
`.vue` 文件通常由三個部分組成：`<template>`、`<script>` 和 `<style>`。這些部分分別負責不同的功能：
*   **`<template>`**：這部分用於定義組件的 HTML 結構。你可以在這裡使用 Vue 的模板語法來綁定數據和處理事件。
*   **`<script>`**：這部分用於定義組件的邏輯和數據。你可以在這裡導入其他模塊、定義組件的數據、方法和生命周期鉤子等。
*   **`<style>`**（可選）：這部分用於定義組件的樣式。你可以在這裡編寫 CSS 或使用預處理器如 SCSS、LESS 等來定義樣式。
以下是一個簡單的 .vue 文件範例：
    ```html
    <template>
      <div>
        <h1>{{ title }}</h1>
        <button @click="changeTitle">改變標題</button>
      </div>
    </template>
    
    <script>
    export default {
      data() {
        return {
          title: 'Hello Vue!'
        }
      },
      methods: {
        changeTitle() {
          this.title = '標題已改變'
        }
      }
    }
    </script>
    
    <style scoped>
    h1 {
      color: blue;
    }
    </style>
    ```

    在這個範例中，`<template>` 部分定義了一個包含標題和按鈕的簡單結構；`<script>` 部分定義了組件的數據和方法；`<style>` 部分定義了標題的樣式，並使用了 `scoped` 屬性來確保樣式只應用於當前組件。

## 快速開始
> Prerequisites:
> Install [Node.js](https://nodejs.org/) version 18.3 or higher

依序執行 `cml`:
`npm create vue@latest`

接著依序依照需要選擇以下初始化條件
```bash
✔ Project name: … <your-project-name>
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes
✔ Add Vitest for Unit testing? … No / Yes
✔ Add an End-to-End Testing Solution? … No / Cypress / Nightwatch / Playwright
✔ Add ESLint for code quality? … No / Yes
✔ Add Prettier for code formatting? … No / Yes
✔ Add Vue DevTools 7 extension for debugging? (experimental) … No / Yes

Scaffolding project in ./<your-project-name>... Done.
```

成功後進到專案目錄下載 `pkg` 後即可開始開發
```bash
cd <your-project-name> 
npm install 
npm run dev
```
