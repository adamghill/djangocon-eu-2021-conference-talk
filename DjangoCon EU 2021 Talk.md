# How to create a fullstack, reactive website in Django with absolutely no JavaScript

## Intro

(Front of the field notes notebook)

Hello! I'm Adam Hill and I'm here to tell you about my journey to find a mythical creature.

Based on the titles of other talks for this conference and the number of questions I see while lurking in the Django sub-reddit, it appears that others are looking for this mythical creature as well!

Now... many believed it doesn't really exist.

But, similar to my search for a friendly Yeti, I'm pretty sure I've at least seen a glimpse of it!

So, follow along with my field notebook while I document what I find!

(Waving Yeti saying hello)

Well, there's one mythical creature, but not exactly what I was looking for!

The mythical creature I was searching for allows Django developers to build a modern, reactive website without writing _any_ custom JavaScript.

Don't get me wrong, JavaScript is _fine_. Sometimes it's even "not that bad".

However, I have run into a few roadblocks trying to integrate a JavaScript frontend with Django.

There is the paradigm switch, not to mention the syntax differences, from synchronous Python to asynchronous JavaScript.

There is the high potential for duplicated business logic between the frontend and the backend.

There is the task of creating a REST or GraphQL API solely for the frontend.

There is the performance hit on first time page load speeds when the frontend framework is parsed, especially with slower machines or network connections.

There is making sure the site is SEO-friendly.

Plus, there is the age-old...

(Vampire)

...keeping up to date with JavaScript build tools.

I could have just given up on my dream of finding this mythical creature.

But, I am pretty stubborn.

I couldn't escape the allure of less complexity, a simpler architecture, faster development time, and... let’s be honest... less code.

It sounds like a wonderful land of rainbows and sunshine.

(Mythical land of rainbows and waterfalls)

*Especially* when some intrepid explorers have already found similar mythical creatures.

## Explorers from other lands

For example, in the land of `Phoenix`, `LiveView` provides frontend interactivity using the backend language, `Elixir`. Because of the robust support for asynchronous processes, it uses websockets to communicate backend changes to the frontend.

(Phoenix)

In the land of `Laravel`, `Livewire` provides a frontend framework using `PHP` and regular ole' HTTP calls. It has extensive documentation and screencasts demonstrating all of its capabilities.

(Leperchaun)

In the land of `Rails`, `Hotwire` made a splash when it was released. It provides frontend interactivity using `Ruby` and websockets to communicate backend changes to the frontend.

(Gremlin with wires)

Some explorers even want to traverse across different lands. `HTMX` which is the successor to `intercooler.js` isn't tied to a particular server-side language and is a lightweight way to provide interactivity without writing any custom JavaScript. Highly recommended! It's really fun to use.

## Django

--> START HERE at HTMX slide 

But, this _is_ DjangoCon, so we should talk about the land of Django, right?! So, let's get CRACKING!

(Kraken on a computer)

First, I'll briefly go over some code for a sample Django + Vue.js integration. Then, I'll show a few Django packages that can create a modern, interactive website without writing any JavaScript.

(django slide overview)

The packages we'll look at code for are Sockpuppet, reactor, and finally... Unicorn. 

But, first, VueJS.

### Django + Vue.js integration

(VueJS slide)

I realize that there are lots of ways to integrate Django with a frontend framework, so the specific code doesn't matter too much -- this is more to show an example of what might be required when integrating with Django. React would have different details, but the general gist would be the same.

Alright, time to live code!

Nah, I'm just kidding!

But, we are going to look over this sample todo app I created.

(Demo VueJS)

The first thing to realize is that most of the time on your local machine you will have two processes running for your site to render properly. One for the Django backend and one Node process for the frontend.

#### Django

This is the typical Django dev server. It provides an API (usually REST or GraphQL).

It also provides the beloved Django admin to easily create, update and delete data from the database.

And, lastly, Django serves a static HTML page that contains the shell of the website with navigation, basic site structure, footers, etc., although sometimes Node will handle that.

Alright, let's look at the code required for the backend. Starting at the urls, we can see that Django is serving the index route and Django REST Framework is providing an "api" route with the `TodoViewSet`.

Let's look at that view set. It contains a queryset property that returns all todo models from the database serialized with this `TodoSerializer`.

The serializer uses this `Todo` model and outputs the primary key and the task for the `Todo`. Serializers are also where the validation of business logic would occur in Django REST Framework.

Django REST Framework creates a nice interface that lets you interact with the API.

[Show browser with API interface]

Let's look at all of the current todos. None yet!

Alright, let's look at the actual site functionality. 

Well, this seems to be missing something. Oh, right! Remember, we need to start up a Node process for things to work as expected?

#### Node

The Node process watches the frontend code and transpiles it for browsers to handle. Here it's using `yarn`, but there are about a dozen different ways to do this.

[yarn serve in terminal]

[Refresh browser]

That looks better!

[Type "Search the ocean", Press "Add"]

Nice, this looks great! Let's check out the frontend to see what is involved to build out this straight-forward example.

[VS Code]

Ok. Here is the index page that is served by Django. You can see it's pretty minimal and contains a `div` element where the application is mounted with the id "app".

The real magic starts `main.js` where you can see the router, store and render method.

Let's look at the router first which stipulates what URLs are handled by Vue. This will also override any urls setup in Django. You can see for this example, the root URL is handled by a component named "todos".

Let's look at the "Todos" component.

It looks... like HTML, but it has some fun, new attributes.

For example, this `v-model` is used by Vue to bind this input element to some `task` data. This `@click` binds the button to an `addTodo` JavaScript method with an argument of the input element above.

And here is how to check for any available `todos` with `v-if` and loop over them with `v-for`. 

It's all in the excellent VueJS documentation, but it's definitely different than the server-side rendered Django templates.

At the bottom of this component is a reference to the store. It is the central location that retrieves and creates todos.

It calls this method here [todos.js].

Which, in turn, calls a service method.

Which, finally, calls the backend Django API.

(VueJS slide)

Again, this overview isn't meant to explain all the specifics of how Vue works, it's more to show a typical setup when integrating a frontend framework with Django and all of its complexities.

I haven't even gotten to choosing (and keeping up with) a JavaScript bundler, deciding how to host the backend and frontend, or picking one of the many options to authenticate users.

Phew!

#### Benefits

So, that all sounds very complicated (because it is!), but there some benefits to this approach: it can be useful to split up the responsibilities of a team. It also provides a contract between frontend and backend to communicate to each other.

And, let's be honest, choosing a mainstream frontend framework that is well documented and supported allows for easier hiring, an ecosystem of libraries that work well with the framework, and the ability to find at least some answers to your pleas for help on StackOverflow.

### Other options

However, if the typical VueJS integration is any mythical creature... maybe it's a Hydra?! There definitely seem like there lots of pieces to wrangle and try to keep track of.

Unfortunately, I am not Hercules.

So, I kept searching and found a few other options for Django developers who don't want to wrestle with that additional complexity.

#### sockpuppet

The first Django library is `sockpuppet`. 

(Sockpuppet slide)

It was originally inspired by the Rail's library `StimulusReflex`. It uses  the `StimulusJS` library and websockets to communicate changes from the frontend to the backend and vice versa.

It is based on the concept of a `Reflex` which encompasses the round-trip lifecycle which gets initiated via data attributes in HTML. Let's see how that works with the sample todo app.

[Show Sockpuppet demo]

Just like the VueJS example, there is a `Todo` model with one field, `Task`, which will store everything we have to do.

Alright, let me fire up the Django dev server. Ok, here you can see that sockpuppet is using ASGI and Django Channels under the hood.

Let's look at the website. Looks pretty similar to the VueJS example.

Let's try it out. [Type in "Search in the woods", press "Add"]

Seems to work!

Now, let's look at the rest of the code.

`todo.py` contains the view that handles this request. It is wired up like any other class-based view in `urls.py`. And you can see it inherits from `TemplateView` so `get_context_data` should look familiar if you've ever used a class-based view before.

This is where the initial state for the view is defined and passed into the view context. You can see I'm getting a list of all of the todo objects and it will be available as a template variable with the name "todos".

Alright, let's look at how that gets rendered in the template. You can use the typical Django template language to loop over each todo and render each task.

Now, let's look at how new tasks are added. This is where `Reflexes` come in to handle mutations of the current state. First, let's look at the frontend to see how the events are defined.

You can see this `data-reflex` attribute on the `input` element here. `keyup` is the browser event, `TodoReflex` is the `Reflex` class, and `new_task` is the method that gets called every time a key is pressed in the input.

And for this `button` element, you can see it is bound to the `add_todo` method.

Let's look at the code to see how that works.

You can see the `new_task` method which will get the input element's value and add it to the session.

The `add_todo` method that gets called when the button is clicked will get the new task from the session, create the `Todo` model, and save it to the database.

Since we are already rendering all `todos` in a list, when a new `Todo` is saved to the database, it will show up automatically in the list.

That's pretty magical!

Let's see the network requests to see a glimpse of how it works behind-the-scenes. You can the websockets connections here in the developer toolbar. And you can even see the method names as part of the websocket packet.

[End of Sockpuppet demo]

`Sockpuppet` is well-documented and brings reactive capabilities to Django and a logical approach, while leveraging the battle-tested `StimulusJS` library.

#### reactor

Another library that brings interactivity to Django is `Reactor`.

(reactor slide)

It uses websockets and its own custom JavaScript library to communicate between the frontend and backend.

Let's look at a sample todo app for `reactor`.

[Show demo of reactor]

You can see the `reactor` demo uses the same `Todo` model with a task field just like the other examples.

Alright, let me start the Django development server. Again, you can see that it uses ASGI and Django Channels for the websockets which are used to communicate state changes from the frontend to the backend.

Let's try it out in the browser. 

[Type "Search the mountain", please "Add"]

Nice! It looks like it's working as expected.

Now, let's look at the code to see the details.

Reactor has the concept of "components" that encapsulate some interactive functionality on a website. You can see the `component` templatetag here on the `index.html` page. You can think of the `component` templatetag almost like an include templatetag. Here it is referring to a component named `x-todo`.

The `x-todo` component should look pretty familiar. It has familiar-looking Django template code and looks likes a regular template. Let's look at how to call methods in our component.

Here's the input which is listening for the `keyup` browser event. It calls a method for `task` in the component backend and passes along a value named `new_task`.

Let's also look at the button here. `@click` specifies the browser event to listen to, the `prevent` modifier calls `preventDefault` on the event to cancel it from triggering like usual.

Now let's look at the backend code. `Reactor` looks for components in a file named `live.py`. Here you can see the `XTodo` component that is the backend code.

The first thing to note is this `mount` method which loads the initial state of the component when it is rendered. Here we see I'm getting all the `Todos` from the database and setting them to a `todos` variable on an instance of the component.

The second thing to note is that the methods specified in the frontend will be prepended with "receive_" in the component. This `receive_task` method was specified as `task` by the input element on the frontend. Everytime there is a `keyup` event on that input element it will update this `new_task` variable.

The `receive_add_todo` method will get called when the "Add" button is clicked from the frontend. The `new_task` instance variable will be used to create a new `Todo` in the database, and then I clear out `new_task` and re-retrieve all of the `Todos` from the database.

Similarly to `sockpuppet`, the list of todos on the frontend will automatically be updated when `self.todos` is set.

Let's look at the network requests again to see the websockets network traffic. 

[Type in "Search the lake", press "Add"]

That's awesome to see how well that works.

[End demo]

`Reactor` uses Vue-like attributes for specifying backend actions in frontend HTML. It's very straight-forward to understand what is supposed to happen from the developer-perspective.

#### Still searching

Both of these Django libraries are impressive, but they also weren't the mythical creature that *I* was searching for.

So, while bored at the beginning of the pandemic, I stopped searching and finally created my own project. I named it `Unicorn` (Unicorn) as a homage to the unofficial pony mascot of Django and because of how magical it felt while prototyping the code.

#### Unicorn

Let's see how our sample todo app would look like in `Unicorn`.

(Unicorn demo in browser)

[Type in "Search the skies", press "Add"]

Well, this looks _very_ familiar!

Let's check out the code to see how Unicorn apporoaches interactivity.

(Unicorn code demo)

Here is the index page. You can see here that `Unicorn` also has the concept of components. And here I made a component named "todo".

Let's look at the todo component's template.

Rendering the current tasks is similar to our other Django solutions where we have access to our normal Django template syntax: if statements, for loops, and anything else you would be able to do with normal Django templates are available.

Well, let's see how the inputs elements work now.

This looks pretty familiar, right? Here is the input element for our task and notice the "unicorn:model" attribute. That will specify what field in our backend component will be bound to this input. In this case, the field name will be "task".

Before looking at the backend, though, let's look at the button real quick. This "unicorn:click" attribute tells `Unicorn` to bind the "add_todo" backend method to the "click" browser event.

Alright, let's look at how this works in the component's view backend.

You can see that backend views sub-class `UnicornView`. Under the hood, it sub-classes `TemplateView`, so the process of switching from a standard `TemplateView` classe-based view should be straight-forward.

Remember when I said that the input element was bound to the "task" field? Here it is on the view. I use types pretty extensively in `Unicorn` to help specify some information about the fields, but they are completely optional.

Hydrate

Method

Ok, let's look at how this works.

(Open up browser and network inspector)

You can see here that an HTTP call is firing for each keypress, passing a JSON payload to an endpoint, and then passing a JSON response back.

If you see that and get concerned about the network traffic latency, `Unicorn` has a few other tricks up its sleeve.

Bound models can have a `lazy` modifier that only fires an HTTP call when the element loses focus. Or a `defer` modifier that only calls the method when an action event fires.

I'll show you what I mean in the browser.

I've slowly added features `Unicorn` over the past year like polling, loading, nested components, and tight integration with Django database models and QuerySets. And because the code is all server-side, unit testing the components is straight-forward and authentication uses the built-in Django functionality.

(Unicorn slide)

## Benefits

`Unicorn` provides everything I need for a modern website quickly without extra complexity. No custom JavaScript, no additional APIs, no JavaScript bundling, no additional processes to run while developing on local, and no requirement on Django Channels.

It's quick to add into an existing site and make it feel a little more interactive.

## Drawbacks

The Django projects I have mentioned most likely won't supplant the need for React or Vue anytime soon. However, in my wanderings, most websites don't need anything that complicated. Most sites are well-served by a server-side Django website with some interactivity sprinkled on top.

If you truly need an SPA, then by all means, definitely stick with one of the major frontend frameworks.

## Call to action

I think I speak for all of the projects mentioned when I say that they are only as helpful as the community around them.

(Elves)

I'd love for you to help *any* of these projects any way you can -- staring their repo, trying them out on a new project, creating issues, updating documentation, or even sponsoring the developers.

## Fin

Well, hopefully that was informative and a little bit fun.

(Fin)

I'm `adamghill` on GitHub if you want the sample code,  slides, or the transcript. And I'm the same username on Twitter. And feel free to reach out if you want to talk about Django, Python, or JavaScript.

(Yeti waving goodbye)

I'd also like to thank my co-workers at The Motley Fool who gave feedback on this talk and my lovely wife, Lynn, who did all of the art for the slides.
