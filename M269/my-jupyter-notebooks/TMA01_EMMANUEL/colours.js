var head=document.getElementsByTagName('head')[0],style = document.createElement('style'),css = '.answercell{background-color: #ffffcc;}.feedbackcell{background-color: #c8ecff;}.guidancecell{background-color: #f2c0d4;}';head.appendChild(style);style.type = 'text/css';style.appendChild(document.createTextNode(css));Jupyter.notebook.get_cells().map(function(cell) {if (cell.metadata['cellcol']!= undefined) {cell.element.addClass(cell.metadata['cellcol']);}});