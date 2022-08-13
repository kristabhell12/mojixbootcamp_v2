import streamlit as st
import streamlit.components.v1 as components
from PIL import Image





st.set_page_config(page_title="entregable1 Mojix", page_icon=":tada:", layout="wide")

left_column, right_column = st.columns(2)
with left_column:
    img = Image.open("pranjal.png")
    st.image(img, width=50)
    st.subheader("Pranjal Saxena :wave:")
with right_column:
    components.html("""
<style type="text/css">
#ayudadeblogger ul {margin:5px 7px;padding:0px;}
#ayudadeblogger ul li {list-style-type: none;padding: 0;background: transparent;margin: 0;}
#ayudadeblogger ul li a{background: url('http://2.bp.blogspot.com/-JKB0aVYaIW0/UC-oBl8NXxI/AAAAAAAAEYA/IbgyikdkM5A/s1600/blsocial12.png') 0 0 no-repeat;   height:48px;padding-left: 48px;cursor: pointer;text-decoration: none;border-radius:0.5em;-moz-border-radius:0.5em;-webkit-border-radius:0.5em;-o-border-radius:0.5em;display:inline-block;margin:0;width: 220px;}

#ayudadeblogger ul li:hover span {margin-left: 5px;opacity: 1;}
#ayudadeblogger ul li span {border-radius:10px;
-moz-border-radius:5px;
-webkit-border-radius:5px;
color: white;
margin-left: 50px;
opacity: 0;
position: relative;
text-align: center;
width: auto;
padding: 2px 5px;
transition: all 0.3s cubic-bezier(1,2,0,0) 0s;
-moz-transition: all 0.3s cubic-bezier(1,2,0,0) 0s;
-webkit-transition: all 0.3s cubic-bezier(1,2,0,0) 0s;
top: 7px;}
#ayudadeblogger span{padding:3px;background:#000;color:#fff;margin:0 3px;}
#ayudadeblogger .fb span {background-color: #0853A3;}

#ayudadeblogger .twiter span {background-color: #00B1F7;}

#ayudadeblogger .google span {background-color: #9E0202;}
#ayudadeblogger .pint span {background-color: #D00;}
#ayudadeblogger .linkedin span {background-color: #005075;}
#ayudadeblogger .devart span {background-color: #4C7A4A;}
#ayudadeblogger .ytube span {background-color: #A00;}
#ayudadeblogger .rss span {background-color: #EC5601;}
#ayudadeblogger a.fb {  background-position: 0 -384px;}
#ayudadeblogger a.twiter {  background-position: 0 -432px;}
#ayudadeblogger a.google {  background-position: 0 -480px;}
#ayudadeblogger a.pint {  background-position: 0 -528px;}
#ayudadeblogger a.linkedin {  background-position: 0 -576px;}
#ayudadeblogger a.devart { background-position: 0 -624px;}
#ayudadeblogger a.ytube {  background-position: 0 -672px;}
#ayudadeblogger a.rss {  background-position: 0 -720px;}
#ayudadeblogger a.fb:hover { background-position: 0 0px;color: #0374DD;}
#ayudadeblogger a.twiter:hover {  background-position: 0 -48px;color: #00A1DF;}
#ayudadeblogger a.google:hover {  background-position: 0 -96px;color: #A70000;}
#ayudadeblogger a.pint:hover {  background-position: 0 -144px;color: #C00;}
#ayudadeblogger a.linkedin:hover {  background-position: 0 -192px;color: #005772;}
#ayudadeblogger a.devart:hover { background-position: 0 -240px;color: #4C7A4A;}
#ayudadeblogger a.ytube:hover {  background-position: 0 -288px;color: #A00;}
#ayudadeblogger a.rss:hover {  background-position: 0 -336px;color: #EC5601;}
</style>

<div id="ayudadeblogger">
<ul>
   <li ><a href="https://www.facebook.com/pages/GrupoDelecluse/116336675191122" class="icon fb" ><span>Visítanos en Facebook</span></a></li>
   <li ><a href="https://twitter.com/grupodelecluse" class="icon twiter" ><span>Recomiéndanos en Twitter</span></a></li>

   <li ><a href="https://plus.google.com/104165660096684906208" class="icon google" ><span>Síguenos en Google +</span></a></li>

   <li ><a href="http://www.pinterest.com/luischavez/" class="icon pint" ><span>Pinterest</span></a></li>
   <li ><a href="http://ec.linkedin.com/pub/luis-chavez/53/549/a91/" class="icon linkedin" ><span>Contáctame en LinkedIn</span></a></li>
   <li ><a href="http://www.deviantart.com/" class="icon devart" ><span>DeviantArt</span></a></li>
   <li ><a href="http://www.youtube.com/" class="icon ytube" ><span>Youtube</span></a></li>
   <li ><a href="http://feeds.feedburner.com/ForoAyudaDeBlogger" class="icon rss" ><span>Suscríbete a nuestro RSS</span></a></li>
</ul>
</div>
    """)       

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.write("Simple but effective tips for every python lovers")
   

img = Image.open("PRUEBA.png")
st.image(img, width=400)


st.write("The compactness of Python can make a developer’s life a lot easier when")
st.write("writing lines and lines of code. But there are some lesser-known Python tricks")
st.write("that can surprise you with their amazing capabilities.")

st.write("In today’s article, I will discuss 10 Python tips and tricks that will be really")
st.write(" helpful for beginners to write more compact code. Knowing these tips and")
st.write("tricks will definitely save you some valuable time.")

st.write("                              .   .   .                         ")

st.subheader("1. Walrus operator")
st.write("The Walrus or := operator is one of the latest additions to python 3.8. It is an")
st.write("assignment operator that lets you assign value to a variable within an")
st.write("expression like conditional statements, loops, etc.")

components.html("<i>Example<i/>")

st.write("If we want to check and print the length of a list:")

img = Image.open("1.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("2.png")
st.image(img, width=300)

st.subheader("2. Splitting a string")
st.write("If you want to split the components of a string into a list you can do that easily")
st.write("using the split() function in python. This will make the string operations a lot")
st.write("easier!")

components.html("<i>Example<i/>")

img = Image.open("3.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("4.png")
st.image(img, width=300)

st.subheader("3. Reversing a string")
st.write("If you want to reverse a given string, you can do that with only one line of code")
st.write("using the negative indexing of the string.")

components.html("<i>Example<i/>")

img = Image.open("5.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("6.png")
st.image(img, width=300)

st.subheader("4. Merging two dictionaries")
st.write("This amazing trick will help you merge two dictionaries with just 1 line of code.")
st.write("We just need to use ** in front of the name of the two dictionaries like below")
st.write("two merge them into a single dictionary:")

components.html("<i>Example<i/>")

img = Image.open("7.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("8.png")
st.image(img, width=300)

st.subheader("5. The zip() function")
st.write("The zip() function in python can make your life a lot easier when working with")
st.write("lists and dictionaries. It is used to combine several lists of the same length.")

components.html("<i>Example<i/>")

img = Image.open("9.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("10.png")
st.image(img, width=300)

st.write("The zip() function can also be used for combining two lists into a dictionary.")
st.write("This method can be really helpful while grouping data from the list.")

components.html("<i>Example<i/>")

img = Image.open("11.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("12.png")
st.image(img, width=300)

st.subheader("6. Assigning multiple list values to a variable")
st.write("If you want to assign some specific values of a list to a variable and all the")
st.write("remaining values to another variable in a list format, you can use the following")
st.write("technique:")

components.html("<i>Example<i/>")

img = Image.open("13.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("14.png")
st.image(img, width=300)

st.write("This process is also called list unpacking and you can apply this method for")
st.write("more than 2 variables also!")

st.subheader("7. Remove duplicate list items")
st.write("Do you have duplicate items in your list which you want to remove? You can")
st.write("do that with only one line of code using the set() function.")

components.html("<i>Example<i/>")

img = Image.open("15.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("16.png")
st.image(img, width=300)

st.subheader("8. Lambda function")
st.write("If you need a function that is not very complicated, it can be done easily in one")
st.write("line using lambda. They are also called anonymous functions and are used")
st.write("heavily in data science and web development.")

components.html("<i>Example<i/>")

st.write("Let’s say you want to write a function to multiply two numbers. Instead of")
st.write("writing a conventional function, you can do that in one line using :")

img = Image.open("17.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("18.png")
st.image(img, width=300)

st.subheader("9. Swapping variable value")
st.write("One of the first programs that we learn while learning about variables is")
st.write("swapping the values of two variables. In python you can achieve that with one")
st.write("healine of code:")

components.html("<i>Example<i/>")

img = Image.open("19.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("20.png")
st.image(img, width=300)

st.subheader("10. Use a password in your code")
st.write("This python trick is amazing for securing your code with a password. We will")
st.write("use the getpass() function from the library getpass which encodes your")
st.write("input. This will prevent anyone from running the code without a password.")
st.write("Isn’t that cool!")

components.html("<i>Example<i/>")

img = Image.open("21.png")
st.image(img, width=300)

st.write("Output")

img = Image.open("22.png")
st.image(img, width=300)

st.write("Here is [a book](https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922?dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1602697607&sr=8-2&linkCode=sl1&tag=pranjal20-20&linkId=71b2efa5db080e8f74068aebec7d7fb0&language=en_US&ref_=as_li_ss_tl) on Python programming that I would definitely")
st.write("recommend for all beginners.")

st.write("                              .   .   .                         ")

st.subheader("Conclusion")

st.write("These were a few amazing Python tips and tricks which will make your work a")
st.write("lot easier while coding. There are many more shortcuts like these that you can")
st.write("explore from the official documentation or any other website.")

st.write("Note: This article contains an affiliate link. This means that if you click on it")
st.write("and choose to buy the resource I linked above, a small portion of your")
st.write("subscription fee will go to me.")

st.write("However, the recommended resource is experienced by me and helped me in")
st.write("my data science career journey.")
st.write(".  .  .")


st.write("Before you go…")

st.write("If you liked this article and want to stay tuned with more exciting articles on")
st.write("Python & Data Science — do consider becoming a medium member by")
st.write("clicking here https://pranjalai.medium.com/membership.")

st.write("Please do consider signing up using [my referral link](https://pranjalai.medium.com/membership). In this way, the portion of")
st.write("the membership fee goes to me, which motivates me to write more exciting")
st.write("stuff on Python and Data Science.")

st.write("Also, feel free to subscribe to my free newsletter: [Pranjal’s Newsletter.](https://pranjalai.medium.com/subscribe)")

st.write("Thanks to Elliot Gunn")
st.write(".  .  .")


st.write("recommend for all beginners.")







































































