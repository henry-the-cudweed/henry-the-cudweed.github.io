title_var="title"
afterpic_var="afterpic"
beforepic_var="beforepic"
longdate_var="the date"
staff_num_var="num of staff"
volunteer_num_var="num volunteers"
outputfile_var="sliders/test.html"
calflora_link_var="calflora.org" 
calfora_site_var="mg11122"

part1="""<!DOCTYPE html>
<html>
<head>
<title>"""
title = title_var
part2="""</title>
<style>

.container {
  max-width: 800px;
}

#comparison {
	width: 100%;
	padding-bottom: 100%;
	overflow: hidden; 
  position: relative;
}

figure { 
  position: absolute;
	background-image: url("""
afterpic = afterpic_var
part3=");"

part4="""	background-size: cover;
	font-size: 0;
	width: 100%;
	height: 100%;
	margin: 0; 
}

#divisor { 
	background-image: url("""

beforepic = beforepic_var

part5=");"
part6="""	background-size: cover;
	position: absolute;
	width: 50%; 
	box-shadow: 0 5px 10px -2px rgba(0,0,0,0.3);
	bottom: 0; height: 100%;
  
  &::before,
  &::after {
    content: '';
    position: absolute;
    right: -2px;
    width: 4px;
    height: calc(50% - 25px);
    background: white;
    z-index: 3;
  }
  &::before {
    top: 0;
    box-shadow: 0 -3px 8px 1px rgba(0,0,0,.3);
  }
  &::after {
    bottom: 0;
    box-shadow: 0 3px 8px 1px rgba(0,0,0,.3);
  }
}
#handle {
  position: absolute;
  height: 50px;
  width: 50px;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
  z-index: 1;
  
  &::before,
  &::after {
    content: '';
    width: 0;
    height: 0;
    border: 6px inset transparent;
    position: absolute;
    top: 50%;
    margin-top: -6px;
  }
  &::before {
    border-right: 6px solid white;
    left: 50%;
    margin-left: -17px;
  }
  &::after {
    border-left: 6px solid white;
    right: 50%;
    margin-right: -17px;
  }
}

input[type=range]{
	-webkit-appearance:none;
	-moz-appearance:none;
	position: absolute;
	top: 50%; left: -25px;
  transform: translateY(-50%);
	background-color: transparent;
	width: calc(100% + 50px); 
  z-index: 2;
  
  &:focus,
  &:active {
    border: none;
    outline: none;
  }
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  border: none;
  height: 50px;
  width: 50px;
  border-radius: 50%;
  background: transparent;
  border: 4px solid white;
  box-shadow: 0 0 8px 1px rgba(0,0,0,.3);
}
input[type=range]::-moz-range-track {
	-moz-appearance:none;
	height:15px;
	width: 100%;
	background-color: transparent; 
	position: relative;
	outline: none;    
}


</style>
<body>


<center>
<div class="container">
  <div id="comparison">
    <figure>
      <div id="handle"></div>
      <div id="divisor"></div>
    </figure>
    <input type="range" min="0" max="100" value="50" id="slider" oninput="moveDivisor()">
  </div>
 </div>
 </center>
 <center>
 <div>
 Move center circle left and right to view site progress.
 <br>
 <br>
 Workday, """
longdate=longdate_var
part7="."
part8=" <br>"
staff_num=staff_num_var
part9=" Staff, "
volunteer_num=volunteer_num_var
part10=" Volunteers."
part11="""
 
 <Br>
  <br>
 
  <a href="
"""
calflora_link=calflora_link_var 

part12="""">Calflora ID """

calflora_site=calfora_site_var
part13="""</a>
</center>
  <!--this part adds a google form, i don't yet know how to format this to look nice, and this may not be the form to use, this is just a test-->
  <!--<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSer8DvzxQEHUvLRI3earx5XStmioJEOuzfN_T6IU6WGO0_zdg/viewform?embedded=true" width="270" height="100%" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>!-->
    <script>
var divisor = document.getElementById("divisor"),
    handle = document.getElementById("handle"),
    slider = document.getElementById("slider");

function moveDivisor() {
  handle.style.left = slider.value+"%";
	divisor.style.width = slider.value+"%";
}

window.onload = function() {
	moveDivisor();
};
</script>
"""

outputfile = outputfile_var

subs= (part1 + title + part2 + afterpic + part3 + part4 + beforepic + part5 + 
part6 + longdate + part7 +  part8 + staff_num + part9 + volunteer_num +part10 + part11 + calflora_link + part12 + calflora_site + part13 )


with open(outputfile,'w') as f: f.write(subs)





