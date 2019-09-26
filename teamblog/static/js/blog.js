window.onload=function(){
    var index=0;
    var parents = document.getElementById('banner')
    var child = parents.children;
    setInterval(changePic,1000);
    function changePic(){
        child[index].style.display = 'none';
        index++;
        if(index==3){
        index=0; }
        child[index].style.display = 'block'
}
$.get('checkPow/',function(data) {
        if(data.stu==1){
           return
        }
        else{
           alert(data.msge)}
    },'json')
}
