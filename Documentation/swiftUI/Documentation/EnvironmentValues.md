Initializer

# init()

Creates an environment values instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## Discussion

You don’t typically create an instance of `EnvironmentValues` directly. Doing
so would provide access only to default values that don’t update based on
system settings or device characteristics. Instead, you rely on an environment
values’ instance that SwiftUI manages for you when you use the `Environment`
property wrapper and the `environment(_:_:)` view modifier.

## See Also

### Creating and accessing values

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`subscript<T>(T.Type) -> T?`

Reads an observable object of the specified type from the environment.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`var description: String`

A string that represents the contents of the environment values instance.

Instance Subscript

# subscript(_:)

Accesses the environment value associated with a custom key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : EnvironmentKey { get set }

## Overview

Create custom environment values by defining a key that conforms to the
`EnvironmentKey` protocol, and then using that key with the subscript operator
of the `EnvironmentValues` structure to get and set a value for that key:

You use custom environment values the same way you use system-provided values,
setting a value with the `environment(_:_:)` view modifier, and reading values
with the `Environment` property wrapper. You can also provide a dedicated view
modifier as a convenience for setting the value:

## See Also

### Creating and accessing values

`init()`

Creates an environment values instance.

`subscript<T>(T.Type) -> T?`

Reads an observable object of the specified type from the environment.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`var description: String`

A string that represents the contents of the environment values instance.

Instance Subscript

# subscript(_:)

Reads an observable object of the specified type from the environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<T>(objectType: T.Type) -> T? where T : AnyObject, T : Observable { get set }

##  Parameters

`objectType`

    

The type of the `Observable` object to read from the environment.

## Return Value

The environment object of the specified type, or `nil` if no object of that
type has been set in this environment.

## Overview

Important

This subscript only supports reading objects that conform to the `Observable`
protocol.

Use this subscript to read the environment object of a specific type from an
instance of `EnvironmentValues`, such as when accessing the `environment`
property of a graphics context:

## See Also

### Creating and accessing values

`init()`

Creates an environment values instance.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`var description: String`

A string that represents the contents of the environment values instance.

Instance Subscript

# subscript(_:)

Accesses the environment value associated with a custom key.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : UITraitBridgedEnvironmentKey { get set }

## Overview

Create custom environment values by defining a key that conforms to the
`EnvironmentKey` protocol, and then using that key with the subscript operator
of the `EnvironmentValues` structure to get and set a value for that key:

You use custom environment values the same way you use system-provided values,
setting a value with the `environment(_:_:)` view modifier, and reading values
with the `Environment` property wrapper. You can also provide a dedicated view
modifier as a convenience for setting the value:

## See Also

### Creating and accessing values

`init()`

Creates an environment values instance.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`subscript<T>(T.Type) -> T?`

Reads an observable object of the specified type from the environment.

`var description: String`

A string that represents the contents of the environment values instance.

Instance Property

# description

A string that represents the contents of the environment values instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var description: String { get }

## See Also

### Creating and accessing values

`init()`

Creates an environment values instance.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

`subscript<T>(T.Type) -> T?`

Reads an observable object of the specified type from the environment.

`subscript<K>(K.Type) -> K.Value`

Accesses the environment value associated with a custom key.

Instance Property

# legibilityWeight

The font weight to apply to text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var legibilityWeight: LegibilityWeight? { get set }

## Discussion

This value reflects the value of the Bold Text display setting found in the
Accessibility settings.

## See Also

### Improving legibility

`var accessibilityShowButtonShapes: Bool`

Whether the system preference for Show Button Shapes is enabled.

`var accessibilityReduceTransparency: Bool`

Whether the system preference for Reduce Transparency is enabled.

`enum LegibilityWeight`

The Accessibility Bold Text user setting options.

Instance Property

# dismiss

An action that dismisses the current presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dismiss: DismissAction { get }

## Discussion

Use this environment value to get the `DismissAction` instance for the current
`Environment`. Then call the instance to perform the dismissal. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

You can use this action to:

  * Dismiss a modal presentation, like a sheet or a popover.

  * Pop the current view from a `NavigationStack`.

  * Close a window that you create with `WindowGroup` or `Window`.

The specific behavior of the action depends on where you call it from. For
example, you can create a button that calls the `DismissAction` inside a view
that acts as a sheet:

When you present the `SheetContents` view, someone can dismiss the sheet by
tapping or clicking the sheet’s button:

Be sure that you define the action in the appropriate environment. For
example, don’t reorganize the `DetailView` in the example above so that it
creates the `dismiss` property and calls it from the
`sheet(item:onDismiss:content:)` view modifier’s `content` closure:

If you do this, the sheet fails to dismiss because the action applies to the
environment where you declared it, which is that of the detail view, rather
than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root
view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If
you need to query whether SwiftUI is currently presenting a view, read the
`isPresented` environment value.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`struct DismissAction`

An action that dismisses a presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Instance Property

# dismissSearch

An action that ends the current search interaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dismissSearch: DismissSearchAction { get }

## Discussion

Use this environment value to get the `DismissSearchAction` instance for the
current `Environment`. Then call the instance to dismiss the current search
interaction. You call the instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance.

When you dismiss search, SwiftUI:

  * Sets `isSearching` to `false`.

  * Clears any text from the search field.

  * Removes focus from the search field.

Note

Calling this instance has no effect if the user isn’t interacting with a
search field.

Use this action to dismiss a search operation based on another user
interaction. For example, consider a searchable view with a `Button` that
presents more information about the first matching item from a collection:

The button becomes visible only after the user enters search text that
produces a match. When the user taps the button, SwiftUI shows a sheet that
provides more information about the item, including an Add button for adding
the item to a stored list of items:

People can dismiss the sheet by dragging it down, effectively canceling the
operation, leaving the in-progress search interaction intact. Alternatively,
people can tap the Add button to store the item. Because the person using your
app is likely to be done with both the detail view and the search interaction
at this point, the button’s closure also uses the `dismiss` property to
dismiss the sheet, and the `dismissSearch` property to reset the search field.

Important

Access the action from inside the searched view, as the example above
demonstrates, rather than from the searched view’s parent, or another
hierarchy, like that of a sheet. SwiftUI sets the value in the environment of
the view that you apply the searchable modifier to, and doesn’t propagate the
value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Property

# dismissWindow

A window dismissal action stored in a view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var dismissWindow: DismissWindowAction { get }

## Discussion

Use the `dismissWindow` environment value to get an `DismissWindowAction`
instance for a given `Environment`. Then call the instance to dismiss a
window. You call the instance directly because it defines a
`callAsFunction(id:)` method that Swift calls when you call the instance.

For example, you can define a button that dismisses an auxiliary window:

## See Also

### Closing windows

`struct DismissWindowAction`

An action that dismisses a window associated to a particular scene.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`struct DismissBehavior`

Programmatic window dismissal behaviors.

Instance Property

# openImmersiveSpace

An action that presents an immersive space.

visionOS 1.0+

    
    
    var openImmersiveSpace: OpenImmersiveSpaceAction { get }

## Discussion

Use this environment value to get the instance of the
`OpenImmersiveSpaceAction` structure for a given `Environment`. Then call the
instance to present a space. You call the instance directly because it defines
`callAsFunction()` methods that Swift calls when you call the instance.

For example, you can define a button that opens a specified planet in an
immersive space:

You indicate which immersive space to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter.

  * A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.

  * Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error
occurs. You can check for errors by inspecting the call’s return value, which
is of type `OpenImmersiveSpaceAction.Result`. For example, the call returns an
error if you already have an immersive space open, because the system enables
only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure
receives a binding to the value that you provide. For best performance, use
lightweight data for the presentation value. For structured model values that
conform to `Identifiable`, the value’s identifier makes a good presentation
value, like the `planet.ID` value in the above code.

## See Also

### Opening an immersive space

`struct OpenImmersiveSpaceAction`

An action that presents an immersive space.

Instance Property

# dismissImmersiveSpace

An immersive space dismissal action stored in a view’s environment.

visionOS 1.0+

    
    
    var dismissImmersiveSpace: DismissImmersiveSpaceAction { get }

## Discussion

Use this environment value to get a `DismissImmersiveSpaceAction` instance for
a given `Environment`. Then call the instance to dismiss a space. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

The asynchronous call returns after the system finishes dismissing the space.
Unlike the call to `openImmersiveSpace` that you use to open the space — which
requires an identifier, a value, or both to specify which space to open — the
dismiss action requires no parameters because there can be only one immersive
space open at a time. The call closes the space that is currently open, if
any.

## See Also

### Closing the immersive space

`struct DismissImmersiveSpaceAction`

An action that dismisses an immersive space.

Instance Property

# newDocument

An action in the environment that presents a new document.

macOS 13.0+

    
    
    var newDocument: NewDocumentAction { get }

## Discussion

Use the `newDocument` environment value to get the instance of the
`NewDocumentAction` structure for a given `Environment`. Then call the
instance to present a new document. You call the instance directly because it
defines a `callAsFunction(_:)` method that Swift calls when you call the
instance.

For example, you can define a button that creates a new document from the
selected text:

The above example assumes that you define a `TextDocument` that conforms to
the `FileDocument` or `ReferenceFileDocument` protocol, and a `DocumentGroup`
that handles the associated file type.

## See Also

### Opening a document programmatically

`struct NewDocumentAction`

An action that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`struct OpenDocumentAction`

An action that presents an existing document.

Instance Property

# openDocument

An action in the environment that presents an existing document.

macOS 13.0+

    
    
    var openDocument: OpenDocumentAction { get }

## Discussion

Use the `openDocument` environment value to get the instance of the
`OpenDocumentAction` structure for a given `Environment`. Then call the
instance to present an existing document. You call the instance directly
because it defines a `callAsFunction(at:)` method that Swift calls when you
call the instance.

For example, you can create a button that opens the document at the specified
URL:

The above example uses a `do-catch` statement to handle any errors that the
open document action might throw. It also places the action inside a task and
awaits the result because the action operates asynchronously.

To present an existing document, your app must define a `DocumentGroup` that
handles the content type of the specified file. For a document that’s already
open, the system brings the existing window to the front. Otherwise, the
system opens a new window.

## See Also

### Opening a document programmatically

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`struct NewDocumentAction`

An action that presents a new document.

`struct OpenDocumentAction`

An action that presents an existing document.

Instance Property

# openURL

An action that opens a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var openURL: OpenURLAction { get set }

## Discussion

Read this environment value to get an `OpenURLAction` instance for a given
`Environment`. Call the instance to open a URL. You call the instance directly
because it defines a `callAsFunction(_:)` method that Swift calls when you
call the instance.

For example, you can open a web site when the user taps a button:

If you want to know whether the action succeeds, add a completion handler that
takes a Boolean value. In this case, Swift implicitly calls the
`callAsFunction(_:completion:)` method instead. That method calls your
completion handler after it determines whether it can open the URL, but
possibly before it finishes opening the URL. You can add a handler to the
example above so that it prints the outcome to the console:

The system provides a default open URL action with behavior that depends on
the contents of the URL. For example, the default action opens a Universal
Link in the associated app if possible, or in the user’s default web browser
if not.

You can also set a custom action using the `environment(_:_:)` view modifier.
Any views that read the action from the environment, including the built-in
`Link` view and `Text` views with markdown links, or links in attributed
strings, use your action. Initialize an action by calling the `init(handler:)`
initializer with a handler that takes a URL and returns an
`OpenURLAction.Result`:

SwiftUI translates the value that your custom action’s handler returns into an
appropriate Boolean result for the action call. For example, a view that uses
the action declared above receives `true` when calling the action, because the
handler always returns `handled`.

## See Also

### Sending and receiving URLs

`struct OpenURLAction`

An action that opens a URL.

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

Instance Property

# openWindow

A window presentation action stored in a view’s environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var openWindow: OpenWindowAction { get }

## Discussion

Use the `openWindow` environment value to get an `OpenWindowAction` instance
for a given `Environment`. Then call the instance to open a window. You call
the instance directly because it defines a `callAsFunction(id:)` method that
Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

You indicate which scene to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter, as in the above example.

  * A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.

  * Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type like a `UUID`.

Use the first option to target either a `WindowGroup` or a `Window` scene in
your app that has a matching identifier. For a `WindowGroup`, the system
creates a new window for the group. If the window group presents data, the
system provides the default value or `nil` to the window’s root view. If the
targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a `WindowGroup` and provide a value to
present. If the interface already has a window from the group that’s
presenting the specified value, the system brings the window to the front.
Otherwise, the system creates a new window and passes a binding to the
specified value.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var supportsMultipleWindows: Bool`

A Boolean value that indicates whether the current platform supports opening
multiple windows.

`struct OpenWindowAction`

An action that presents a window.

Instance Property

# purchase

An action that starts an in-app purchase.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    var purchase: PurchaseAction { get }

## Discussion

Read this environment value to get an `PurchaseAction` instance for a given
`Environment`. Call the instance to start an in-app purchase. You call the
instance directly because it defines a
`PurchaseAction/callAsFunction(_:options:)` method that Swift calls when you
call the instance.

For example, you can start an in-app purchase when the user taps a button:

## See Also

### Actions

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`var openImmersiveSpace: OpenImmersiveSpaceAction`

An action that presents an immersive space.

`var dismissImmersiveSpace: DismissImmersiveSpaceAction`

An immersive space dismissal action stored in a view’s environment.

`var newDocument: NewDocumentAction`

An action in the environment that presents a new document.

`var openDocument: OpenDocumentAction`

An action in the environment that presents an existing document.

`var openURL: OpenURLAction`

An action that opens a URL.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`var resetFocus: ResetFocusAction`

An action that requests the focus system to reevaluate default focus.

Instance Property

# refresh

A refresh action stored in a view’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var refresh: RefreshAction? { get }

## Discussion

When this environment value contains an instance of the `RefreshAction`
structure, certain built-in views in the corresponding `Environment` begin
offering a refresh capability. They apply the instance’s handler to any
refresh operation that the user initiates. By default, the environment value
is `nil`, but you can use the `refreshable(action:)` modifier to create and
store a new refresh action that uses the handler that you specify:

On iOS and iPadOS, the `List` in the example above offers a pull to refresh
gesture because it detects the refresh action. When the user drags the list
down and releases, the list calls the action’s handler. Because SwiftUI
declares the handler as asynchronous, it can safely make long-running
asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the `refresh`
environment value to get the `RefreshAction` instance for a given
`Environment`. If you find a non-`nil` value, change your view’s appearance or
behavior to offer the refresh to the user, and call the instance to conduct
the refresh. You can call the refresh instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance:

Be sure to call the handler asynchronously by preceding it with `await`.
Because the call is asynchronous, you can use its lifetime to indicate
progress to the user. For example, you can reveal an indeterminate
`ProgressView` before calling the handler, and hide it when the handler
completes.

If your code isn’t already in an asynchronous context, create a `Task` for the
method to run in. If you do this, consider adding a way for the user to cancel
the task. For more information, see Concurrency in _The Swift Programming
Language_.

## See Also

### Refreshing a list’s content

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`struct RefreshAction`

An action that initiates a refresh operation.

Instance Property

# rename

An action that activates the standard rename interaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var rename: RenameAction? { get }

## Discussion

Use the `renameAction(_:)` modifier to configure the rename action in the
environment.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Property

# resetFocus

An action that requests the focus system to reevaluate default focus.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    var resetFocus: ResetFocusAction { get }

## Discussion

Get this environment value and call and call it as a function to force a
default focus reevaluation at runtime.

## See Also

### Resetting focus

`struct ResetFocusAction`

An environment value that provides the ability to reevaluate default focus.

Instance Property

# authorizationController

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

AuthenticationServices  SwiftUI  iOS 16.4+  iPadOS 16.4+  macOS 13.3+  tvOS
16.4+  watchOS 9.4+

    
    
    var authorizationController: AuthorizationController { get }

## Discussion

For example, you can perform authorization requests when the user taps a
button:

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

`var webAuthenticationSession: WebAuthenticationSession`

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

Instance Property

# webAuthenticationSession

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

AuthenticationServices  SwiftUI  iOS 16.4+  iPadOS 16.4+  macOS 13.3+  tvOS
16.4+  watchOS 9.4+

    
    
    var webAuthenticationSession: WebAuthenticationSession { get }

## Discussion

For example, you can start a web authentication session when the user taps a
button:

Use `WebAuthenticationSession/BrowserSession/ephemeral` to request that the
browser doesn’t share cookies or other browsing data between the
authentication session and the user’s normal browser session. Whether the
request is honored depends on the user’s default web browser. Safari always
honors the request.

After the user authenticates, the authentication provider redirects the
browser to a URL that uses the callback scheme. The browser detects the
redirect, dismisses itself, and the complete URL will be returned. Inspect the
URL to determine the outcome of the authentication:

The above example looks for a token stored as a query parameter. The specific
parsing that you have to do depends on how the authentication provider
structures the callback URL.

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

`var authorizationController: AuthorizationController`

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

Instance Property

# buttonRepeatBehavior

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var buttonRepeatBehavior: ButtonRepeatBehavior { get }

## Discussion

A value of `enabled` means that buttons will be able to repeatedly trigger
their action, and `disabled` means they should not. A value of `automatic`
means that buttons will defer to default behavior.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Property

# controlSize

The size to apply to controls within a view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var controlSize: ControlSize { get set }

## Discussion

The default is `ControlSize.regular`.

## See Also

### Sizing controls

`func controlSize(ControlSize) -> some View`

Sets the size for controls within this view.

`enum ControlSize`

The size classes, like regular or small, that you can apply to controls within
a view.

Instance Property

# controlActiveState

The active state of controls in the view.

macOS 10.15+

    
    
    var controlActiveState: ControlActiveState { get set }

## Discussion

The default is `ControlActiveState.key`.

## See Also

### Activating controls

`enum ControlActiveState`

Instance Property

# defaultWheelPickerItemHeight

The default height of an item in a wheel-style picker, such as a date picker.

watchOS 6.0+

    
    
    var defaultWheelPickerItemHeight: CGFloat { get set }

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Property

# keyboardShortcut

The keyboard shortcut that buttons in this environment will be triggered with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var keyboardShortcut: KeyboardShortcut? { get }

## Discussion

This is particularly useful in button styles when a button’s appearance
depends on the shortcut associated with it. On macOS, for example, when a
button is bound to the Return key, it is typically drawn with a special
emphasis. This happens automatically when using the built-in button styles,
and can be implemented manually in custom styles using this environment key:

If no keyboard shortcut has been applied to the view or its ancestor, then the
environment value will be `nil`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Property

# menuIndicatorVisibility

The menu indicator visibility to apply to controls within a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var menuIndicatorVisibility: Visibility { get set }

## Discussion

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of this environment value.

## See Also

### Showing a menu indicator

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

Instance Property

# menuOrder

The preferred order of items for menus presented from this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var menuOrder: MenuOrder { get set }

## Discussion

Set this value for a view hierarchy by calling the `menuOrder(_:)` view
modifier.

## See Also

### Setting a preferred order

`func menuOrder(MenuOrder) -> some View`

Sets the preferred order of items for menus presented from this view.

`struct MenuOrder`

The order in which a menu presents its content.

Instance Property

# searchSuggestionsPlacement

The current placement of search suggestions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var searchSuggestionsPlacement: SearchSuggestionsPlacement { get }

## Discussion

Search suggestions render based on the platform and surrounding context in
which you place the searchable modifier containing suggestions. You can render
search suggestions in two ways:

  * In a menu attached to the search field.

  * Inline with the main content of the app.

You find the current search suggestion placement by querying the
`searchSuggestionsPlacement` in your search suggestions.

In the above example, search suggestions only render in iOS if the searchable
modifier displays them in a menu. You might want to do this to render
suggestions in your own list alongside your own search results when they would
render in a list.

## See Also

### Controls and input

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`var controlSize: ControlSize`

The size to apply to controls within a view.

`var controlActiveState: ControlActiveState`

The active state of controls in the view.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

Instance Property

# colorScheme

The color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorScheme: ColorScheme { get set }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using the `ColorScheme.light` or
`ColorScheme.dark` appearance. The value that you receive depends on whether
the user has enabled Dark Mode, possibly superseded by the configuration of
the current presentation’s view hierarchy.

You can set the `colorScheme` environment value directly, but that usually
isn’t what you want. Doing so changes the color scheme of the given view and
its child views but _not_ the views above it in the view hierarchy. Instead,
set a color scheme using the `preferredColorScheme(_:)` modifier, which also
propagates the value up through the view hierarchy to the enclosing
presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider
also checking the `colorSchemeContrast` property, which reflects a system-wide
contrast setting that the user controls. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Detecting and requesting the light or dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Instance Property

# colorSchemeContrast

The contrast associated with the color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorSchemeContrast: ColorSchemeContrast { get }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using `ColorSchemeContrast.standard` or
`ColorSchemeContrast.increased` contrast. The value that you read depends
entirely on user settings, and you can’t change it.

When adjusting your app’s user interface to match the contrast, consider also
checking the `colorScheme` property to find out if SwiftUI is displaying the
view with a light or dark appearance. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Getting the color scheme contrast

`enum ColorSchemeContrast`

The contrast between the app’s foreground and background colors.

Instance Property

# displayScale

The display scale of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var displayScale: CGFloat { get set }

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# horizontalSizeClass

The horizontal size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var horizontalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of horizontal space available to
the view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

  * The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on this size class. For
example, a `NavigationView` presents a multicolumn view when the horizontal
size class is `UserInterfaceSizeClass.regular`, but a single column otherwise.
You can also adjust the appearance of custom views by reading the size class
and conditioning your views. If you do, be prepared to handle size class
changes while your app runs, because factors like device orientation can
change at runtime.

In watchOS, the horizontal size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the horizontal size class in the environment before macOS 14.0,
tvOS 17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# imageScale

The image scale for this environment.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var imageScale: Image.Scale { get set }

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Instance Property

# pixelLength

The size of a pixel on the screen.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var pixelLength: CGFloat { get }

## Discussion

This value is usually equal to `1` divided by `displayScale`.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# sidebarRowSize

The current size of sidebar rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var sidebarRowSize: SidebarRowSize { get set }

## Discussion

On macOS, reflects the value of the “Sidebar icon size” in System Settings’
Appearance settings.

This can be used to update the content shown in the sidebar in response to
this size. And it can be overridden to force a sidebar to a particularly size,
regardless of the user preference.

On other platforms, the value is always `.medium` and setting a different
value has no effect.

SwiftUI views like `Label` automatically adapt to the sidebar row size.

## See Also

### Configuring the sidebar

`enum SidebarRowSize`

The standard sizes of sidebar rows.

Instance Property

# verticalSizeClass

The vertical size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var verticalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of vertical space available to the
view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

You can adjust the appearance of custom views by reading this size class and
conditioning your views. If you do, be prepared to handle size class changes
while your app runs, because factors like device orientation can change at
runtime.

In watchOS, the vertical size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the vertical size class in the environment before macOS 14.0, tvOS
17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# calendar

The current calendar that views should use when handling dates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var calendar: Calendar { get set }

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`struct MultiDatePicker`

A control for picking multiple dates.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

Instance Property

# documentConfiguration

The configuration of a document in a `DocumentGroup`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var documentConfiguration: DocumentConfiguration? { get }

## Discussion

The value is `nil` for views that are not enclosed in a `DocumentGroup`.

For example, if the app shows the document path in the footer of each
document, it can get the URL from the environment:

## See Also

### Accessing document configuration

`struct DocumentConfiguration`

Instance Property

# locale

The current locale that views should use.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var locale: Locale { get set }

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Property

# managedObjectContext

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var managedObjectContext: NSManagedObjectContext { get set }

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Instance Property

# modelContext

The SwiftData model context that will be used for queries and other model
operations within this environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    var modelContext: ModelContext { get set }

## See Also

### Global objects

`var calendar: Calendar`

The current calendar that views should use when handling dates.

`var documentConfiguration: DocumentConfiguration?`

The configuration of a document in a `DocumentGroup`.

`var locale: Locale`

The current locale that views should use.

`var managedObjectContext: NSManagedObjectContext`

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

`var undoManager: UndoManager?`

The undo manager used to register a view’s undo operations.

Instance Property

# timeZone

The current time zone that views should use when handling dates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var timeZone: TimeZone { get set }

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`struct MultiDatePicker`

A control for picking multiple dates.

`var calendar: Calendar`

The current calendar that views should use when handling dates.

Instance Property

# undoManager

The undo manager used to register a view’s undo operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var undoManager: UndoManager? { get }

## Discussion

This value is `nil` when the environment represents a context that doesn’t
support undo and redo operations. You can skip registration of an undo
operation when this value is `nil`.

## See Also

### Storing document data in a class instance

`protocol ReferenceFileDocument`

A type that you use to serialize reference type documents to and from file.

`struct ReferenceFileDocumentConfiguration`

The properties of an open reference file document.

Instance Property

# isScrollEnabled

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isScrollEnabled: Bool { get set }

## Discussion

The default value is `true`. Use the `scrollDisabled(_:)` modifier to
configure this property.

## See Also

### Disabling scrolling

`func scrollDisabled(Bool) -> some View`

Disables or enables scrolling in scrollable views.

Instance Property

# horizontalScrollIndicatorVisibility

The visibility to apply to scroll indicators of any horizontally scrollable
content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility { get set }

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Property

# verticalScrollIndicatorVisibility

The visiblity to apply to scroll indicators of any vertically scrollable
content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility { get set }

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Property

# scrollDismissesKeyboardMode

The way that scrollable content interacts with the software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode { get set }

## Discussion

The default value is `automatic`. Use the `scrollDismissesKeyboard(_:)`
modifier to configure this property.

## See Also

### Interacting with a software keyboard

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`struct ScrollDismissesKeyboardMode`

The ways that scrollable content can interact with the software keyboard.

Instance Property

# horizontalScrollBounceBehavior

The scroll bounce mode for the horizontal axis of scrollable views.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    var horizontalScrollBounceBehavior: ScrollBounceBehavior { get set }

## Discussion

Use the `scrollBounceBehavior(_:axes:)` view modifier to set this value in the
`Environment`.

## See Also

### Configuring scroll bounce behavior

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Property

# verticalScrollBounceBehavior

The scroll bounce mode for the vertical axis of scrollable views.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    var verticalScrollBounceBehavior: ScrollBounceBehavior { get set }

## Discussion

Use the `scrollBounceBehavior(_:axes:)` view modifier to set this value in the
`Environment`.

## See Also

### Configuring scroll bounce behavior

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Property

# editMode

An indication of whether the user can edit the contents of a view associated
with this environment.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    var editMode: Binding<EditMode>? { get set }

## Discussion

Read this environment value to receive a optional binding to the edit mode
state. The binding contains an `EditMode` value that indicates whether edit
mode is active, and that you can use to change the mode. To learn how to read
an environment value, see `EnvironmentValues`.

Certain built-in views automatically alter their appearance and behavior in
edit mode. For example, a `List` with a `ForEach` that’s configured with the
`onDelete(perform:)` or `onMove(perform:)` modifier provides controls to
delete or move list items while in edit mode. On devices without an attached
keyboard and mouse or trackpad, people can make multiple selections in lists
only when edit mode is active.

You can also customize your own views to react to edit mode. The following
example replaces a read-only `Text` view with an editable `TextField`,
checking for edit mode by testing the wrapped value’s `isEditing` property:

You can set the edit mode through the binding, or you can rely on an
`EditButton` to do that for you, as the example above demonstrates. The button
activates edit mode when the user taps the Edit button, and disables editing
mode when the user taps Done.

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Property

# isActivityFullscreen

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    var isActivityFullscreen: Bool { get }

## Discussion

When a Live Activity fills the entire screen, the system extends the
background tint color you set with the `activityBackgroundTint(_:)` modifier
to fill the screen.

Note that this environment variable is always `false` in iOS 16.

## See Also

### Configuring a Live Activity

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

Instance Property

# isEnabled

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Property

# isFocused

Returns whether the nearest focusable ancestor has focus.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var isFocused: Bool { get }

## Discussion

If there is no focusable ancestor, the value is `false`.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Property

# isHoverEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    var isHoverEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Property

# isLuminanceReduced

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isLuminanceReduced: Bool { get set }

## Discussion

When you detect this condition, lower the overall brightness of your view. For
example, you can change large, filled shapes to be stroked, and choose less
bright colors:

In addition to the changes that you make, the system could also dim the
display to achieve a suitable brightness. By reacting to `isLuminanceReduced`,
you can preserve contrast and readability while helping to satisfy the reduced
brightness requirement.

Note

On watchOS, the system typically sets this value to `true` when the user
lowers their wrist, but the display remains on. Starting in watchOS 8, the
system keeps your view visible on wrist down by default. If you want the
system to blur the screen instead, as it did in earlier versions of watchOS,
set the value for the `WKSupportsAlwaysOnDisplay` key in your app’s
Information Property List file to `false`.

## See Also

### Reacting to interface characteristics

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# isPresented

A Boolean value that indicates whether the view associated with this
environment is currently presented.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isPresented: Bool { get }

## Discussion

You can read this value like any of the other `EnvironmentValues` by creating
a property with the `Environment` property wrapper:

Read the value inside a view if you need to know when SwiftUI presents that
view. For example, you can take an action when SwiftUI presents a view by
using the `onChange(of:initial:_:)` modifier:

This behaves differently than `onAppear(perform:)`, which SwiftUI can call
more than once for a given presentation, like when you navigate back to a view
that’s already in the navigation hierarchy.

To dismiss the currently presented view, use `dismiss`.

## See Also

### Dismissing a presentation

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Instance Property

# isSceneCaptured

The current capture state.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var isSceneCaptured: Bool { get set }

## Discussion

Use this value to determine whether the scene is actively being cloned to
another destination (like during AirPlay) or is being mirrored or recorded.

Your app can respond to changes in this value to take appropriate action, like
obscuring content.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# isSearching

A Boolean value that indicates when the user is searching.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isSearching: Bool { get }

## Discussion

You can read this value like any of the other `EnvironmentValues`, by creating
a property with the `Environment` property wrapper:

Get the value to find out when the user interacts with a search field that’s
produced by one of the searchable modifiers, like
`searchable(text:placement:prompt:)`:

When the user first taps or clicks in a search field, the `isSearching`
property becomes `true`. When the user cancels the search operation, the
property becomes `false`. To programmatically set the value to `false` and
dismiss the search operation, use `dismissSearch`.

Important

Access the value from inside the searched view, as the example above
demonstrates, rather than from the searched view’s parent. SwiftUI sets the
value in the environment of the view that you apply the searchable modifier
to, and doesn’t propagate the value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Property

# scenePhase

The current phase of the scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var scenePhase: ScenePhase { get set }

## Discussion

The system sets this value to provide an indication of the operational state
of a scene or collection of scenes. The exact meaning depends on where you
access the value. For more information, see `ScenePhase`.

## See Also

### Monitoring scene life cycle

`enum ScenePhase`

An indication of a scene’s operational state.

Instance Property

# supportsMultipleWindows

A Boolean value that indicates whether the current platform supports opening
multiple windows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var supportsMultipleWindows: Bool { get }

## Discussion

Read this property from the environment to determine if your app can use the
`openWindow` action to open new windows:

The reported value depends on both the platform and how you configure your
app:

  * In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.

  * In iPadOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key `UIApplicationSupportsMultipleScenes` set to `true`.

  * For all other platforms and configurations, the value returns `false`.

If the value is false and you try to open a window, SwiftUI ignores the action
and logs a runtime error.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

`struct OpenWindowAction`

An action that presents a window.

Instance Property

# displayStoreKitMessage

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    var displayStoreKitMessage: DisplayMessageAction { get }

## See Also

### StoreKit configuration

`var requestReview: RequestReviewAction`

Instance Property

# requestReview

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
visionOS 1.0+

    
    
    @MainActor
    var requestReview: RequestReviewAction { get }

## See Also

### StoreKit configuration

`var displayStoreKitMessage: DisplayMessageAction`

Instance Property

# allowsTightening

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var allowsTightening: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Property

# autocorrectionDisabled

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var autocorrectionDisabled: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Property

# dynamicTypeSize

The current Dynamic Type size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dynamicTypeSize: DynamicTypeSize { get set }

## Discussion

This value changes as the user’s chosen Dynamic Type size changes. The default
value is device-dependent.

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

On macOS, this value cannot be changed by users and does not affect the text
size.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Property

# font

The default font of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var font: Font? { get set }

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`struct Font`

An environment-dependent font.

Instance Property

# layoutDirection

The layout direction associated with the current environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var layoutDirection: LayoutDirection { get set }

## Discussion

Use this value to determine or set whether the environment uses a left-to-
right or right-to-left direction.

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Instance Property

# lineLimit

The maximum number of lines that text can occupy in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineLimit: Int? { get set }

## Discussion

The maximum number of lines is `1` if the value is less than `1`. If the value
is `nil`, the text uses as many lines as required. The default is `nil`.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

Instance Property

# lineSpacing

The distance in points between the bottom of one line fragment and the top of
the next.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineSpacing: CGFloat { get set }

## Discussion

This value is always nonnegative.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Property

# minimumScaleFactor

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var minimumScaleFactor: CGFloat { get set }

## Discussion

In the example below, a label with a `minimumScaleFactor` of `0.5` draws its
text in a font size as small as half of the actual font if needed to fit into
the space next to the text input field:

You can set the minimum scale factor to any value greater than `0` and less
than or equal to `1`. The default value is `1`.

SwiftUI uses this value to shrink text that doesn’t fit in a view when it’s
okay to shrink the text. For example, a label with a `minimumScaleFactor` of
`0.5` draws its text in a font size as small as half the actual font if
needed.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Property

# multilineTextAlignment

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var multilineTextAlignment: TextAlignment { get set }

## Discussion

Set this value for a view hierarchy by applying the
`multilineTextAlignment(_:)` view modifier. Views in the hierarchy that
display text, like `Text` or `TextEditor`, read the value from the environment
and adjust their text alignment accordingly.

This value has no effect on a `Text` view that contains only one line of text,
because a text view has a width that exactly matches the width of its widest
line. If you want to align an entire text view rather than its contents, set
the aligment of its container, like a `VStack` or a frame that you create with
the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
modifier.

Note

You can use this value to control the alignment of a `Text` view that you
create with the `init(_:style:)` initializer to display localized dates and
times, including when the view uses only a single line, but only when that
view appears in a widget.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

Instance Property

# textCase

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var textCase: Text.Case? { get set }

## Discussion

The default value is `nil`, displaying the `Text` without any case changes.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Property

# truncationMode

A value that indicates how the layout truncates the last line of text to fit
into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var truncationMode: Text.TruncationMode { get set }

## Discussion

The default value is `Text.TruncationMode.tail`. Some controls, however, might
have a different default if appropriate.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Property

# allowedDynamicRange

The allowed dynamic range for the view, or nil.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var allowedDynamicRange: Image.DynamicRange? { get set }

## See Also

### View attributes

`var backgroundMaterial: Material?`

The material underneath the current view.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var physicalMetrics: PhysicalMetricsConverter`

The physical metrics associated with a scene.

`var realityKitScene: Scene?`

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

Instance Property

# backgroundMaterial

The material underneath the current view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var backgroundMaterial: Material? { get set }

## Discussion

This value is `nil` if the current background isn’t one of the standard
materials. If you set a material, the standard content styles enable their
vibrant rendering modes.

You set this value by calling one of the background modifiers that takes a
`ShapeStyle`, like `background(_:ignoresSafeAreaEdges:)` or
`background(_:in:fillStyle:)`, and passing in a `Material`. You can also set
the value manually, using `nil` to disable vibrant rendering, or a `Material`
instance to enable the vibrancy style associated with the specified material.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Property

# backgroundProminence

The prominence of the background underneath views associated with this
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var backgroundProminence: BackgroundProminence { get set }

## Discussion

Foreground elements above an increased prominence background are typically
adjusted to have higher contrast against a potentially vivid color, such as
taking on a higher opacity monochrome appearance according to the
`colorScheme`. System styles like `primary`, `secondary`, etc will
automatically resolve to an appropriate style in this context. The property
can be read and used for custom styled elements.

In the example below, a custom star rating element is in a list row alongside
some text. When the row is selected and has an increased prominence
appearance, the text and star rating will update their appearance, the star
rating replacing its use of yellow with the standard `secondary` style.

Note that the use of `backgroundProminence` was used by a view that was nested
in additional stack containers within the row. This ensured that the value
correctly reflected the environment within the list row itself, as opposed to
the environment of the list as a whole. One way to ensure correct resolution
would be to prefer using this in a custom ShapeStyle instead, for example:

Views like `List` and `Table` as well as standard shape styles like
`ShapeStyle.selection` will automatically update the background prominence of
foreground views. For custom backgrounds, this environment property can be
explicitly set on views above custom backgrounds.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Property

# backgroundStyle

An optional style that overrides the default system background style when set.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var backgroundStyle: AnyShapeStyle? { get set }

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Property

# badgeProminence

The prominence to apply to badges associated with this environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var badgeProminence: BadgeProminence { get set }

## Discussion

The default is `standard`.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Property

# contentTransition

The current method of animating the contents of views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransition: ContentTransition { get set }

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# contentTransitionAddsDrawingGroup

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransitionAddsDrawingGroup: Bool { get set }

## Discussion

Setting this value to `true` causes SwiftUI to wrap content transitions with a
`drawingGroup(opaque:colorMode:)` modifier.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# defaultMinListHeaderHeight

The default minimum height of a header in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListHeaderHeight: CGFloat? { get set }

## Discussion

When this value is `nil`, the system chooses the appropriate height. The
default is `nil`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

Instance Property

# defaultMinListRowHeight

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListRowHeight: CGFloat { get set }

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

Instance Property

# isFocusEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isFocusEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Configuring effects

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

Instance Property

# headerProminence

The prominence to apply to section headers within a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var headerProminence: Prominence { get set }

## Discussion

The default is `Prominence.standard`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Property

# physicalMetrics

The physical metrics associated with a scene.

visionOS 1.0+

    
    
    var physicalMetrics: PhysicalMetricsConverter { get }

## Discussion

Reading this value returns a `PhysicalMetricsConverter` corresponding to the
window scene associated with the environment’s reader. The converter can
convert point sizes into physical measurements of length, and vice versa.

Reading this value is only supported in the body of a `View` or of a type that
inherits a `View`’s environment.

## See Also

### View attributes

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

`var backgroundMaterial: Material?`

The material underneath the current view.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var realityKitScene: Scene?`

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

Instance Property

# realityKitScene

RealityKit  SwiftUI  visionOS 1.0+

    
    
    var realityKitScene: Scene? { get }

## See Also

### View attributes

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

`var backgroundMaterial: Material?`

The material underneath the current view.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var physicalMetrics: PhysicalMetricsConverter`

The physical metrics associated with a scene.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

Instance Property

# redactionReasons

The current redaction reasons applied to the view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var redactionReasons: RedactionReasons { get set }

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# springLoadingBehavior

The behavior of spring loaded interactions for the views associated with this
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var springLoadingBehavior: SpringLoadingBehavior { get }

## Discussion

Spring loading refers to a view being activated during a drag and drop
interaction. On iOS this can occur when pausing briefly on top of a view with
dragged content. On macOS this can occur with similar brief pauses or on
pressure-sensitive systems by “force clicking” during the drag. This has no
effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation
effect, allowing the destination to be revealed without pausing the drag
interaction. For example, a button that reveals a list of folders that a
dragged item can be dropped onto.

A value of `enabled` means that a view should support spring loaded
interactions if it is able, and `disabled` means it should not. A value of
`automatic` means that a view should follow its default behavior, such as a
`TabView` automatically allowing spring loading, but a `Picker` with
`segmented` style would not.

## See Also

### Configuring spring loading

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

Instance Property

# symbolRenderingMode

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbolRenderingMode: SymbolRenderingMode? { get set }

## See Also

### Setting symbol rendering modes

`func symbolRenderingMode(SymbolRenderingMode?) -> some View`

Sets the rendering mode for symbol images within this view.

`struct SymbolRenderingMode`

A symbol rendering mode.

Instance Property

# symbolVariants

The symbol variant to use in this environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbolVariants: SymbolVariants { get set }

## Discussion

You set this environment value indirectly by using the `symbolVariant(_:)`
view modifier. However, you access the environment variable directly using the
`environment(_:_:)` modifier. Do this when you want to use the `none` variant
to ignore the value that’s already in the environment:

## See Also

### Setting a symbol variant

`func symbolVariant(SymbolVariants) -> some View`

Makes symbols within the view show a particular variant.

`struct SymbolVariants`

A variant of a symbol.

Instance Property

# showsWidgetContainerBackground

An environment variable that indicates whether the background of a widget
appears.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    var showsWidgetContainerBackground: Bool { get }

## Return Value

`true` if, by default, the background appears in this context; `false`
otherwise.

## Discussion

In iOS 16 and earlier, this environment variable is always `true` for system
widgets and `false` for accessory widgets. In macOS 13 and earlier, and in
watchOS 9 and earlier, it always evaluates to `true`.

If you pass `false` to `containerBackgroundRemovable(_:)` to always show the
widget background, the system shows the widget background even if
`showsWidgetContainerBackground` evaluates to `true`.

## See Also

### Widgets

`var showsWidgetLabel: Bool`

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

`var widgetFamily: WidgetFamily`

The template of the widget — small, medium, or large.

`var widgetRenderingMode: WidgetRenderingMode`

The widget’s rendering mode, based on where the system is displaying it.

`var widgetContentMargins: EdgeInsets`

A property that identifies the content margins of a widget.

Instance Property

# showsWidgetLabel

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    var showsWidgetLabel: Bool { get set }

## Discussion

Use this value to determine if you can provide additional content, or possibly
move some of the widget’s content out of the main view and into the widget
label.

This environment value is most useful when defining the appearance for the
`WidgetKit/WidgetFamily/accessoryCircular` widget family, because it’s value
can change depending on where the widget appears. For example, if the widget
is the top circular complication on the Infograph watch face, the value is
`true`. Otherwise it is `false`. The environment variable is always `false` in
iOS.

Other families always have the same value, regardless of where the widget
appears. For the `WidgetKit/WidgetFamily/accessoryCorner` widget family, the
value is always `true`. For other families, it is `false`.

## See Also

### Widgets

`var showsWidgetContainerBackground: Bool`

An environment variable that indicates whether the background of a widget
appears.

`var widgetFamily: WidgetFamily`

The template of the widget — small, medium, or large.

`var widgetRenderingMode: WidgetRenderingMode`

The widget’s rendering mode, based on where the system is displaying it.

`var widgetContentMargins: EdgeInsets`

A property that identifies the content margins of a widget.

Instance Property

# widgetFamily

The template of the widget — small, medium, or large.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var widgetFamily: WidgetFamily { get }

## Overview

Use this value to retrieve the widget size that the user chose for a widget.

## See Also

### Widgets

`var showsWidgetContainerBackground: Bool`

An environment variable that indicates whether the background of a widget
appears.

`var showsWidgetLabel: Bool`

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

`var widgetRenderingMode: WidgetRenderingMode`

The widget’s rendering mode, based on where the system is displaying it.

`var widgetContentMargins: EdgeInsets`

A property that identifies the content margins of a widget.

Instance Property

# widgetRenderingMode

The widget’s rendering mode, based on where the system is displaying it.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var widgetRenderingMode: WidgetRenderingMode { get set }

## Discussion

You can read the rendering mode from the environment values using this key.

Then modify the widget’s appearance based on the mode.

## See Also

### Widgets

`var showsWidgetContainerBackground: Bool`

An environment variable that indicates whether the background of a widget
appears.

`var showsWidgetLabel: Bool`

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

`var widgetFamily: WidgetFamily`

The template of the widget — small, medium, or large.

`var widgetContentMargins: EdgeInsets`

A property that identifies the content margins of a widget.

Instance Property

# widgetContentMargins

A property that identifies the content margins of a widget.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var widgetContentMargins: EdgeInsets { get }

## Return Value

Returns the content margins for the current widget presentation context.

## Discussion

The content margins of a widget depend on the context in which it appears. The
system applies default content margins. However, if you disable automatic
application of default content margins with `contentMarginsDisabled()`, the
system uses the `widgetContentMargins` property in combination with
`View/padding(_)` to selectively apply default content margins.

## See Also

### Widgets

`var showsWidgetContainerBackground: Bool`

An environment variable that indicates whether the background of a widget
appears.

`var showsWidgetLabel: Bool`

A Boolean value that indicates whether an accessory family widget can display
an accessory label.

`var widgetFamily: WidgetFamily`

The template of the widget — small, medium, or large.

`var widgetRenderingMode: WidgetRenderingMode`

The widget’s rendering mode, based on where the system is displaying it.

Instance Property

# disableAutocorrection

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 8.0–10.4  Deprecated  visionOS 1.0+

    
    
    var disableAutocorrection: Bool? { get set }

## Discussion

When the value is `nil`, SwiftUI uses the system default. The default value is
`nil`.

## See Also

### Deprecated environment values

`var sizeCategory: ContentSizeCategory`

The size of content.

Deprecated

`var presentationMode: Binding<PresentationMode>`

A binding to the current presentation mode of the view associated with this
environment.

Deprecated

`struct PresentationMode`

An indication whether a view is currently presented by another view.

Deprecated

Instance Property

# sizeCategory

The size of content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    var sizeCategory: ContentSizeCategory { get set }

Deprecated

Use `dynamicTypeSize` instead.

## See Also

### Deprecated environment values

`var disableAutocorrection: Bool?`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`var presentationMode: Binding<PresentationMode>`

A binding to the current presentation mode of the view associated with this
environment.

Deprecated

`struct PresentationMode`

An indication whether a view is currently presented by another view.

Deprecated

Instance Property

# presentationMode

A binding to the current presentation mode of the view associated with this
environment.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    var presentationMode: Binding<PresentationMode> { get }

Deprecated

Use `isPresented` or `dismiss` instead.

## See Also

### Deprecated environment values

`var disableAutocorrection: Bool?`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`var sizeCategory: ContentSizeCategory`

The size of content.

Deprecated

`struct PresentationMode`

An indication whether a view is currently presented by another view.

Deprecated

Structure

# PresentationMode

An indication whether a view is currently presented by another view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct PresentationMode

Deprecated

Use `isPresented` or `dismiss` instead.

## Topics

### Checking presentation

`var isPresented: Bool`

Indicates whether a view is currently presented.

### Dismissing presentation

`func dismiss()`

Dismisses the view if it is currently presented.

## See Also

### Deprecated environment values

`var disableAutocorrection: Bool?`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`var sizeCategory: ContentSizeCategory`

The size of content.

Deprecated

`var presentationMode: Binding<PresentationMode>`

A binding to the current presentation mode of the view associated with this
environment.

Deprecated

Instance Property

# complicationRenderingMode

The complication rendering mode for the current environment.

ClockKit  SwiftUI  watchOS 7.0–10.4  Deprecated

    
    
    var complicationRenderingMode: ComplicationRenderingMode { get }

Deprecated

On watchOS 9.0 or later, use WidgetKit instead

Instance Property

# immersiveSpaceDisplacement

Provides the pose applied by the system to displace the origin of the
immersive space.

visionOS 1.1+

    
    
    var immersiveSpaceDisplacement: Pose3D { get }

## Discussion

By default, the immersive space is centered on the floor, roughly below the
user’s position. In this case, `.identity` is provided. The center of the
immersive space may be moved by the system to a more appropriate location,
e.g., during a spatial SharePlay experience, in which case this provides the
system-imposed displacement of the immersive space from its original person-
centered position to its new experience- centered position. Inverting the pose
provides the value needed to convert back to the immersive space’s default
location proximate to the user, prior to displacement.

If this property is accessed outside of an open Immersive Space, it provides
`.identity`.

