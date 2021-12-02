$.get('/data/day_1.csv',{},function(content){
    let lines=content.split('\n');

    console.log(`"file.txt" contains ${lines.length} lines`)
    console.log(`First line : ${lines[0]}`)

});
