new ClipboardJS('.btn');

$('#button').on('click', async ()=>{
    // let data = await fetch('https://gist.githubusercontent.com/valibojici/f6806c38994cbbcabe0e3872f0ed15b8/raw/395c4115d6fdaeca10933382868a215301929c84/test2.cpp');
    let data = await fetch('https://raw.githubusercontent.com/valibojici/website-test/main/output.json');
    data = await data.json();
    let code = data.content;
    let solution = data.solution;
    
    console.log(code);
    console.log(solution);

    let lines = code.trim().split('\n').length;
    $("#line-no").text([...Array(lines).keys()].map(i => i + 1).join('\n'))
    


    $("#problem").text(code);

    $("#solution").append($(`<p>${solution}</p>`));
 
    hljs.highlightAll();
})


$('#copy-button').on('click', e =>{
    copyToClipboard('code');
});

function copyToClipboard (containerid) {
    // Create a new textarea element and give it id='temp_element'
    const textarea = document.createElement('textarea')
    textarea.id = 'temp_element'
    // Optional step to make less noise on the page, if any!
    textarea.style.height = 0
    // Now append it to your page somewhere, I chose <body>
    document.body.appendChild(textarea)
    // Give our textarea a value of whatever inside the div of id=containerid
    textarea.value = document.getElementById(containerid).innerText
    // Now copy whatever inside the textarea to clipboard
    const selector = document.querySelector('#temp_element')
    selector.select()
    document.execCommand('copy')
    // Remove the textarea
    document.body.removeChild(textarea)
  }
