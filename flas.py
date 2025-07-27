from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(".")

# HTML Template with Ace Editor
html = """
<!DOCTYPE html>
<html lang="en">
<!-- GET OUT, WHO THE HELL LET YOU IN HERE? -->
<!-- 
Avalon Studio Code - Proprietary License

Copyright (c) [2025] RandomX

All rights reserved.

This software (Avalon Studio Code, also known as ASC) is proprietary and confidential. By using, accessing, or distributing this software, you agree to the following terms:

1. You are not permitted to view, access, reverse engineer, decompile, or otherwise attempt to access the source code in any form.
2. You may not modify, edit, alter, or create derivative works of any part of this software.
3. Redistribution of any kind is prohibited without express written permission from the original author.
4. This software is provided "as is", without any warranties of any kind.

Unauthorized copying, modification, or distribution is strictly prohibited and may result in legal consequences.

For inquiries, contact:

- RandomX
-->
<head>
  <meta charset="UTF-8">
  <title>Avalon Studio Code</title>
  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Orbitron&family=Share+Tech+Mono&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <!-- Styles -->
  <style>
    body {
      background-color: #000;
      color: #ff0000;
      font-family: 'JetBrains Mono', monospace;
      margin: 0;
    }


    #top-bar {
      background: #111;
      padding: 0;
      border-bottom: 1px solid #ff0000;
    }
   
    #file-bar {
      background: #111; /* darker background for contrast */
      border-bottom: 2px double #ff0000;
      height: 35px;
      display: flex;
      align-items: center;
      padding: 0 10px;
      color: #ff0000;
      font-family: 'Orbitron', sans-serif;
      font-size: 14px;
      box-shadow: 0 0 6px #ff0000 inset;
      letter-spacing: 1px;
    }
   
    .file-tab {
      padding: 5px 10px;
      margin-right: 7px;
      background: #222;
      color: #ff0000;
      border: 1px solid #ff0000;
      font-family: 'Orbitron', sans-serif;
      cursor: pointer;
    }
   
    .file-tab:hover {
      background: #333;
      box-shadow: 0 0 6px #ff0000;
    }
   
    .active-tab {
      background: #000;
      font-weight: bold;
      border-bottom: none;
    }
   
    a#file-export {
      background: #222;
      color: #ff0000;
      border: 2px double #ff0000;
      box-shadow: 0 0 4px #ff0000, 0 0 8px #ff0000 inset;
      font-family: 'Orbitron', sans-serif;
      padding: 4px 8px;
      text-decoration: none;
      transition: box-shadow 0.4s ease-in-out, transform 0.2s ease-in-out;
      display: inline-block;
    }
    a#file-export:hover {
      box-shadow: 0 0 10px #ff0000;
      transform: scale(1.03);
      cursor: pointer;
    }


   
    h3 {
      font-family: 'Orbitron', sans-serif;
      color: #ff0000;
      margin: 0;
    }


    #editor {
      height: 90vh;
      width: 100%;
      font-size: 16px;
      font-family: 'Share Tech Mono', monospace;
    }


    select, #file-input, #file-export, #utility, #utility2, #about {
      background: #222;
      color: #ff0000;
      border: 2px double #ff0000;
      box-shadow:
        0 0 4px #ff0000,
        0 0 8px #ff0000 inset;
      margin: 0px;
      padding: 0px;
      font-family: 'Orbitron', sans-serif;
      transform: scale(1);
      transition: box-shadow 0.4s ease-in-out, transform 0.2s ease;
    }
   
    select:hover,
    #file-input:hover,
    #file-export:hover,
    #utility:hover,
    #about:hover,
    #utility2:hover{
      box-shadow: 0 0 10px #ff0000;
      transform: scale(1.03);
      cursor: pointer;
    }
   
    #menu-icon {
      position: absolute;
      top: 10px;
      right: 10px;
      color: #ff0000;
      font-size: 24px;
      cursor: pointer;
    }
   
    #dropdown-menu {
      position: absolute;
      top: 50px;
      right: 50px;
      background: #111;
      border: 1px solid #ff0000;
      padding: 10px;
      height: 70px;
      color: #ff0000;
      font-family: 'Orbitron', sans-serif;
      z-index: 100;
    }
   
    #menu {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: #111;
      color: #ff0000;
      padding: 10px;
      border: 2px solid #ff0000;
      font-family: 'Orbitron', sans-serif;
    }
   
    button {
             background: #222;
          color: #ff0000;
          border: 2px double #ff0000;
          box-shadow:
            0 0 4px #ff0000,
            0 0 8px #ff0000 inset;
          transition: box-shadow 0.5s ease-in-out;
          margin: 0px;
          left: 2px;
          padding: 0px;
          font-family: 'Orbitron', sans-serif;
          transform: scale(1);
          transition: box-shadow 0.4s ease-in-out, transform 0.2s ease;
    }
    button:hover{
      box-shadow: 0 0 10px #ff0000;
      transform: scale(1.03);
      cursor: pointer;
    }
   
    .hidden {
      display: none;
    }
   
    a {
        color: red;
        text-decoration: none; /* optional: remove underline */
        display: inline-block;  /* needed for transform to work properly */
        transform: scale(1);
        transition:
            box-shadow 0.4s ease-in-out,
            transform 0.2s ease-in-out,
            color 0.2s ease-in-out;
    }
   
    a:hover {
        color: blue;
        transform: scale(1.03);
        border: 2px solid #0000ff;
        box-shadow: 0 0 10px #0000ff;
    }
   
    a:visited {
        color: green;
    }
   
   
   
    iframe {
      border: 2px solid #222;
      border: 2px solid #222;
      float: left; /* Aligns to the left */
      margin-right: 10px; /* Optional spacing from content on the right */


    }
   
    .button-link {
      background: #222;
      color: #ff0000;
      border: 2px double #ff0000;
      box-shadow: 0 0 4px #ff0000, 0 0 8px #ff0000 inset;
      font-family: 'Orbitron', sans-serif;
      padding: 4px 10px;
      text-decoration: none;
      display: inline-block;
      transition: 0.3s ease-in-out;
    }
   
    .button-link:hover {
      box-shadow: 0 0 10px #ff0000;
      transform: scale(1.03);
      cursor: pointer;
    }

    #bin-inpt,
    #hex-inpt {
      width: 100%;
      max-width: 500px;
      padding: 10px 15px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      color: #ff0000;
      background-color: #111;
      border: 2px solid #444;
      border-radius: 8px;
      outline: none;
      transition: border-color 0.3s, box-shadow 0.3s;
      margin: 10px 0;
    }
    
    #bin-inpt:focus,
    #hex-inpt:focus {
      border-color: #ff0000;
      box-shadow: 0 0 8px #ff0000;
    }
    
    #lower-bar {
      width: 97.5%;
      padding: 10px 13px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      color: #ff0000;
      background-color: #111;
      border: 2px double #ff0000;
      
      outline: none;
      transition: border-color 0.3s, box-shadow 0.3s;
      margin: 0px 0;
    }
    
    #tab {
      resize: both;
      overflow: auto;
      width: 150px;
      height: 150px;
      background-color: #3498db;
      position: absolute;
      top: 100px;
      left: 100px;
      cursor: move;
      color: white;
      text-align: center;
      line-height: 150px;
      font-family: sans-serif;
      border-radius: 12px;
    }
    
    .hidden {
      display: none;
    }

   
  </style>
  <!-- GET OUT, WHO THE HELL LET YOU IN HERE? -->


  <!-- Ace Editor -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ace.js"></script>
</head>










<body id="body">
  <div id="top-bar">
    <h3>Avalon Studio Code</h3>
    <input id="file-input" type="file">
    <button id="file-export" onclick="exportFile()">
      <i class="fas fa-download"></i> Export
    </button>


   
    <button id="utility" onclick="saveSession()">Save Session</button>
    <button id="utility2" onclick="viewHTML()">View as Html</button>
    <select id="language-selector">
      <option value="auto">Auto</option>
      <option value="py">Python (.py)</option>
      <option value="js">JavaScript (.js)</option>
      <option value="html">HTML (.html)</option>
      <option value="css">CSS (.css)</option>
      <option value="json">JSON (.json)</option>
      <option value="java">Java (.java)</option>
      <option value="c">C (.c)</option>
      <option value="cpp">C++ (.cpp)</option>
      <option value="sh">Shell Script (.sh)</option>
      <option value="md">Markdown (.md)</option>
      <option value="xml">XML (.xml)</option>
      <option value="txt">Plain Text (.txt)</option>
      <option value="ts">TypeScript (.ts)</option>
      <option value="php">PHP (.php)</option>
      <option value="rb">Ruby (.rb)</option>
      <option value="rs">Rust (.rs)</option>
      <option value="jsx">JavaScript React (.jsx)</option>
      <option value="tsx">TypeScript React (.tsx)</option>
      <option value="vue">Vue.js (.vue)</option>
      <option value="swift">Swift (.swift)</option>
      <option value="asm">Assembly (.asm)</option>
      <option value="s">Assembly (.s)</option>
      <option value="yml">YAML (.yml)</option>
      <option value="yaml">YAML (.yaml)</option>
      <option value="dart">Dart (.dart)</option>
      <option value="go">Go (.go)</option>
      <option value="bat">Batch (.bat)</option>
      <option value="ini">INI (.ini)</option>
      <option value="dockerfile">Dockerfile</option>
      <option value="cson">CoffeeScript (.cson)</option>
      <option value="coffee">CoffeeScript (.coffee)</option>
      <option value="sql">SQL (.sql)</option>
      <option value="pl">Perl (.pl)</option>
      <option value="m">Objective-C (.m)</option>
      <option value="mm">Objective-C++ (.mm)</option>
      <option value="lua">Lua (.lua)</option>
    </select>


    <div style="display: flex;">
        <iframe id="html-viewer" width="100%" height="600" style="border: 2px solid red;"></iframe>
    </div>




  </div>
 
  <div id="file-bar">
    <span id="current-file"><i class="fas fa-file-code"></i> Unnamed File</span>
    <button onclick="newFile()">+ New File</button>
  </div>
  
    <div id="lower-bar">
      <button onclick="loadHexElement()">Hexadecimal Converter</button>
      <button onclick="loadBinElement()">Binary Converter</button>
    
      <input id="hex-inpt" type="text" placeholder="Type your string here...(Hex Converter)" style="display: none;">
      <button onclick="showHex()" id="c-hex" style="display: none;">Convert</button>
      <p id="hex-output" style="display: none;">Hex Result:</p>
    
      <input id="bin-inpt" type="text" placeholder="Type your string here...(Binary Converter)" style="display: none;">
      <button onclick="showBin()" id="c-bin" style="display: none;">Convert</button>
      <p id="bin-output" style="display: none;">Binary Result:</p>
    </div>

  <div id="editor"></div>


  <div id="menu-icon" onclick="toggleMenu()">
      <i class="fas fa-bars"></i>
  </div>
   
  <div id="dropdown-menu" class="hidden">
        <p id="menu">Menu</p>
        <a id="about-link" href="about.html" target="_blank">About Avalon Studio Code</a>
  </div>
 
  
  <div id="tab" style="background-color: #111; border: 4px double #ff0000; transition: box-shadow 0.4s ease-in-out, transform 0.2s ease; transform: scale(1); color: #ff0000; position: absolute;">
      <p>shrink this to destroy it
      </p>
  </div>


 
 
 
 


  <!-- JavaScript Section -->
  <script>
      const topBar = document.getElementById("top-bar")
     
  </script> <!-- database section -->
  <script>
    const fileInput = document.getElementById('file-input');
    const output = document.getElementById('editor');
    const reader = new FileReader();


    reader.onload = function (e) {
      editor.setValue(e.target.result, -1); // -1 puts cursor at start
    };


    fileInput.addEventListener('change', function () {
      const file = fileInput.files[0];
      if (!file) return;
      reader.readAsText(file);
    });
  </script> <!-- file input -->
  <script>
    const editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
  </script> <!-- editor-ace -->
  <script>
    function exportFile() {
        const content = editor.getValue();
   
        // Safe fallback name
        let filename = currentFile && typeof currentFile === 'string' ? currentFile : "avalon_code";
   
        // Add extension if missing
        if (!filename.includes(".")) {
            const mode = editor.session.$modeId.split("/").pop();
            const extMap = {
                python: "py", javascript: "js", html: "html", css: "css", json: "json",
                java: "java", c_cpp: "cpp", sh: "sh", markdown: "md", xml: "xml",
                text: "txt", typescript: "ts", php: "php", ruby: "rb", rust: "rs",
                jsx: "jsx", tsx: "tsx", vue: "vue", swift: "swift", assembly_x86: "asm",
                yaml: "yml", dart: "dart", golang: "go", batchfile: "bat", ini: "ini",
                dockerfile: "Dockerfile", coffee: "coffee", sql: "sql", perl: "pl",
                lua: "lua"
            };
            const ext = extMap[mode] || "ASCFileExportation";
            filename += "." + ext;
        }
   
        const blob = new Blob([content], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
   
        // Dynamically create and trigger a download
        const a = document.createElement("a");
        a.href = url;
        a.download = filename;
        a.style.display = "none";
        document.body.appendChild(a);
        a.click();
   
        setTimeout(() => {
            URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }, 1000);
   
        console.log("Export successful:", filename);
    }
  </script> <!-- file export -->
  <script>
    function refresh() {
      editor.setValue("");
    }
  </script> <!-- refresh -->
  <script>
    // Delay warning
    setTimeout(function () {
      console.log("%cDO NOT PASTE ANY MALICIOUS CODE HERE, YOU DON'T KNOW WHAT IT WILL DO!!!", 'color: red; background: black; font-weight: bold; padding: 4px;');
    }, 3000);
  </script> <!-- warning -->
  <script>
      function toggleMenu() {
          const menu = document.getElementById("dropdown-menu");
          menu.classList.toggle("hidden");
      }


  </script> <!-- dropdown menu -->
  <script>
      const fileStorage = {}; // like { "Untitled 1": "print('Hello')" }
      let currentFile = null; // track the active file
     
      function saveSession() {
        localStorage.setItem('avalon_last_code', editor.getValue());
        alert("Session saved!");
      }
     
      setInterval(() => {
          localStorage.setItem("avalon_last_code", editor.getValue());
        }, 10000);
       
      document.addEventListener("DOMContentLoaded", function () {
        const lastCode = localStorage.getItem('avalon_last_code');
        if (lastCode) {
          editor.setValue(lastCode, -1);
        }
      });
     


    let fileCount = 1;


    function newFile() {
        const fileBar = document.getElementById("file-bar");
        const fileName = `Untitled ${fileCount++}`;
        const tab = document.createElement("div");
        tab.className = "file-tab";
        tab.textContent = fileName;
        tab.dataset.fileName = fileName;
        tab.addEventListener("click", () => switchFile(fileName, tab));
        tab.addEventListener("contextmenu", function (e) {
            e.preventDefault();
            renameFile(tab);
        });
        fileBar.appendChild(tab);
        fileStorage[fileName] = "";
        switchFile(fileName, tab);
    }


   
    function switchFile(fileName, tabElement) {
        if (currentFile !== null) {
            fileStorage[currentFile] = editor.getValue();
        }
            editor.setValue(fileStorage[fileName] || "", -1);
            currentFile = fileName;
            setEditorModeByFilename(fileName);
            document.getElementById("current-file").innerHTML = `<i class="fas fa-file-code"></i> ${fileName}`;
   
            // Update file name display
            document.getElementById("current-file").innerHTML = `<i class="fas fa-file-code"></i> ${fileName}`;
       
            document.querySelectorAll(".file-tab").forEach(tab => {
                tab.classList.remove("active-tab");
            });
            tabElement.classList.add("active-tab");
        }
       
    function renameFile(tabElement) {
        if (!currentFile || !tabElement) return;
   
        const newName = prompt("Rename current file:", currentFile);
        if (!newName || newName === currentFile) return;
   
        // Move content in fileStorage
        fileStorage[newName] = fileStorage[currentFile];
        delete fileStorage[currentFile];
   
        // Update tab and current tracking
        tabElement.textContent = newName;
        tabElement.dataset.fileName = newName;
        currentFile = newName;
   
        // Update UI label
        document.getElementById("current-file").innerHTML = `<i class="fas fa-file-code"></i> ${newName}`;
    }


    tab.addEventListener("click", () => switchFile(fileName, tab));


    tab.addEventListener("contextmenu", function (e) {
        e.preventDefault();
        renameFile(tab);
    });


  </script> <!-- file managing -->
  <script>
    let viewerVisible = false;
    function viewHTML() {
        const viewer = document.getElementById("html-viewer");
        const code = editor.getValue(); // Get the current code from the editor
   
        viewerVisible = !viewerVisible;
   
        if (viewerVisible) {
            viewer.srcdoc = code;      // Load HTML
            viewer.style.display = "block"; // Show iframe
        } else {
            viewer.style.display = "none"; // Hide iframe
        }
    }
  </script> <!-- html viewer -->
  <script>
      function setEditorModeByFilename(filename) {
            const extension = filename.split('.').pop().toLowerCase();
            const modeMap = {
                'py': 'python',
                'js': 'javascript',
                'html': 'html',
                'css': 'css',
                'json': 'json',
                'java': 'java',
                'c': 'c_cpp',
                'cpp': 'c_cpp',
                'sh': 'sh',
                'md': 'markdown',
                'xml': 'xml',
                'txt': 'text',
                'ts': 'typescript',
                'php': 'php',
                'rb': 'ruby',
                'rs': 'rust',
                'jsx': 'jsx',
                'tsx': 'tsx', // sometimes jsx fallback
                'vue': 'vue',
                'swift': 'swift',
                'asm': 'assembly_x86',
                's': 'assembly_x86',
                'yml': 'yaml',
                'yaml': 'yaml',
                'dart': 'dart',
                'go': 'golang',
                'bat': 'batchfile',
                'ini': 'ini',
                'dockerfile': 'dockerfile',
                'cson': 'coffee',
                'coffee': 'coffee',
                'sql': 'sql',
                'pl': 'perl',
                'm': 'c_cpp',      // Objective-C
                'mm': 'c_cpp',     // Objective-C++
                'lua': 'lua',
            };
       
            const mode = modeMap[extension] || 'text';
            editor.session.setMode("ace/mode/" + mode);
        }
    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        if (!file) return;
        reader.readAsText(file);
        setEditorModeByFilename(file.name); // 👈 auto detect here
    });
    document.getElementById("language-selector").addEventListener("change", function(e) {
        const selected = e.target.value;
        if (selected !== "auto") {
            editor.session.setMode("ace/mode/" + selected);
        } else {
            setEditorModeByFilename(currentFile); // fallback to auto
        }
    });
  </script> <!-- file mode -->
  <script>
      function stringToHex(str) {
        let hexString = '';
        for (let i = 0; i < str.length; i++) {
          const charCode = str.charCodeAt(i);
          const hex = charCode.toString(16);
          hexString += (hex.length === 1 ? '0' : '') + hex;
        }
        return hexString;
      }
    
      function stringToBinary(inputString) {
        let binaryResult = '';
        for (let i = 0; i < inputString.length; i++) {
          const charCode = inputString.charCodeAt(i);
          const binaryChar = charCode.toString(2);
          const paddedBinaryChar = binaryChar.padStart(8, '0');
          binaryResult += paddedBinaryChar + ' ';
        }
        return binaryResult.trim();
      }
    
      function decodeBinary(binaryString) {
        const binaryChunks = binaryString.split(' ');
        const decodedCharacters = binaryChunks.map(chunk => {
          const decimalValue = parseInt(chunk, 2);
          return String.fromCharCode(decimalValue);
        });
        return decodedCharacters.join('');
      }
    
      function decodeHex(hex) {
        return hex.match(/.{1,2}/g)
          .map(byte => String.fromCharCode(parseInt(byte, 16)))
          .join('');
      }
    
      let visibleHex = false;
      let visibleBin = false;
    
      function loadHexElement() {
        const container = document.getElementById("c-hex");
        const input = document.getElementById("hex-inpt");
        const output = document.getElementById("hex-output");
        const value = input.value;
        const hexVal = stringToHex(value);
    
        visibleHex = !visibleHex;
    
        container.style.display = visibleHex ? "block" : "none";
        input.style.display = visibleHex ? "block" : "none";
        output.style.display = visibleHex ? "block" : "none";
        if (visibleHex) output.innerHTML = hexVal;
      }
    
      function loadBinElement() {
        const container = document.getElementById("c-bin");
        const input = document.getElementById("bin-inpt");
        const output = document.getElementById("bin-output");
        const value = input.value;
        const binVal = stringToBinary(value);
    
        visibleBin = !visibleBin;
    
        container.style.display = visibleBin ? "block" : "none";
        input.style.display = visibleBin ? "block" : "none";
        output.style.display = visibleBin ? "block" : "none";
        if (visibleBin) output.innerHTML = binVal;
      }
    
      function showHex() {
        const value = document.getElementById("hex-inpt").value;
        const result = stringToHex(value);
        document.getElementById("hex-output").innerHTML = "Hex Result: " + result;
      }
    
      function showBin() {
        const value = document.getElementById("bin-inpt").value;
        const result = stringToBinary(value);
        document.getElementById("bin-output").innerHTML = "Bin Result: " + result;
      }
</script> <!-- advanced data types converter -->
  <script>
      const drag = document.getElementById("tab");
      let isDragging = false;
      let offsetX, offsetY;
    
      drag.addEventListener("mousedown", (e) => {
        isDragging = true;
        offsetX = e.clientX - drag.offsetLeft;
        offsetY = e.clientY - drag.offsetTop;
      });
    
      document.addEventListener("mousemove", (e) => {
        if (isDragging) {
          drag.style.left = (e.clientX - offsetX) + "px";
          drag.style.top = (e.clientY - offsetY) + "px";
        }
      });
    
      document.addEventListener("mouseup", () => {
        isDragging = false;
      });
  </script> <!-- make window tab draggable -->
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/list")
def list_files():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".py")]
    return jsonify(files)

@app.route("/load", methods=["POST"])
def load_file():
    filename = request.json.get("filename")
    try:
        with open(os.path.join(BASE_DIR, filename), "r") as f:
            content = f.read()
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/save", methods=["POST"])
def save_file():
    data = request.json
    filename = data.get("filename")
    content = data.get("content")
    try:
        with open(os.path.join(BASE_DIR, filename), "w") as f:
            f.write(content)
        return jsonify({"status": "saved"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
