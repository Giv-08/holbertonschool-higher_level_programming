# DOM manipultaion

![image](https://github.com/user-attachments/assets/f8da2cb6-1289-4067-bde2-080a1eaeb98b)

In web development, one of the main features to enable interactivity is DOM Manipulation. DOM manipulation allows developers to interact and modify the structure, style, and content of web pages dynamically.

### DOM Element Selectors
There are multiple methods available in DOM to select the HTML elements and manipulate them as listed below:

querySelector() method: The querySelector( ) method is used to select the first element that matches the specified selector provided as an argument.
querySelectorAll() method: The querySelectorAll() method returns a NodeList which contains all elements that match the selector within the document.
getElementById( ) method: The getElementId() method is used to select a single element using its Id.
getElementByClassName( ): The getElementsByClassName() method in JavaScript is used to select elements in the HTML document that have a specific class name.
getElementByTagName() method: The getElementsByTagName() method is used to select elements using the specified tag name.
getElementByName() method: The getElementsByName() method is used to select elements that have a specific name attribute. This method returns a NodeList of elements with the specified name.

### DOM content manipulators
The below DOM properties can be used to change the HTML and the text content of the HTML elements.

textContent: The textContent property is used to set and get the text content and it's descendants.
innerHTML: The innerHTML property is used to get and set the text and HTML inside an HTML element.
innerText: The innerText property represents the rendered text content of a node and its descendants. It is aware of the elements which will be rendered and ignores the hidden elements.

### DOM element creators
You can also create dynamic HTML elements using the below DOM methods.

createElement( ) method: The createElement( ) method is used to create an element in the HTML DOM document
appendChild( ) method: The appendChild( ) method is used to append a node to a list of child nodes of a specified parent node.
createTextNode( ) method: The createTextNode( ) method is used to create a text node.

### DOM CSS manipulators
The below DOM properties can be used to manipulate the CSS of the HTML elements.

style: CSS can be manipulated using (Syntax : element.style.propertyName) which helps us to dynamically manipulate styles and access the inline styles of an element.
cssText: CSS can be directly manipulated using the cssText property of the style object to set multiple inline styles at a time. It is similar to how we add inline CSS to an element.
classList: As Inline CSS is not recommended, mostly we use classList property to dynamically add and remove CSS classes which are defined in external CSS.
