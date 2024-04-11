Article

# Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

## Overview

Store data as state in the least common ancestor of the views that need the
data to establish a single _source of truth_ that’s shared across views.
Provide the data as read-only through a Swift property, or create a two-way
connection to the state with a binding. SwiftUI watches for changes in the
data, and updates any affected views as needed.

Don’t use state properties for persistent storage because the life cycle of
state variables mirrors the view life cycle. Instead, use them to manage
transient state that only affects the user interface, like the highlight state
of a button, filter settings, or the currently selected list item. You might
also find this kind of storage convenient while you prototype, before you’re
ready to make changes to your app’s data model.

### Manage mutable values as state

If a view needs to store data that it can modify, declare a variable with the
`State` property wrapper. For example, you can create an `isPlaying` Boolean
inside a podcast player view to keep track of when a podcast is running:

Marking the property as state tells the framework to manage the underlying
storage. Your view reads and writes the data, found in the state’s
`wrappedValue` property, by using the property name. When you change the
value, SwiftUI updates the affected parts of the view. For example, you can
add a button to the `PlayerView` that toggles the stored value when tapped,
and that displays a different image depending on the stored value:

Limit the scope of state variables by declaring them as private. This ensures
that the variables remain encapsulated in the view hierarchy that declares
them.

### Declare Swift properties to store immutable values

To provide a view with data that the view doesn’t modify, declare a standard
Swift property. For example, you can extend the podcast player to have an
input structure that contains strings for the episode title and the show name:

While the value of the episode property is a constant for `PlayerView`, it
doesn’t need to be constant in this view’s parent view. When the user selects
a different episode in the parent, SwiftUI detects the state change and
recreates the `PlayerView` with a new input.

### Share access to state with bindings

If a view needs to share control of state with a child view, declare a
property in the child with the `Binding` property wrapper. A binding
represents a reference to existing storage, preserving a single source of
truth for the underlying data. For example, if you refactor the podcast player
view’s button into a child view called `PlayButton`, you can give it a binding
to the `isPlaying` property:

As shown above, you read and write the binding’s wrapped value by referring
directly to the property, just like state. But unlike a state property, the
binding doesn’t have its own storage. Instead, it references a state property
stored somewhere else, and provides a two-way connection to that storage.

When you instantiate `PlayButton`, provide a binding to the corresponding
state variable declared in the parent view by prefixing it with the dollar
sign (`$`):

The `$` prefix asks a wrapped property for its `projectedValue`, which for
state is a binding to the underlying storage. Similarly, you can get a binding
from a binding using the `$` prefix, allowing you to pass a binding through an
arbitrary number of levels of view hierarchy.

You can also get a binding to a scoped value within a state variable. For
example, if you declare `episode` as a state variable in the player’s parent
view, and the episode structure also contains an `isFavorite` Boolean that you
want to control with a toggle, then you can refer to `$episode.isFavorite` to
get a binding to the episode’s favorite status:

### Animate state transitions

When the view state changes, SwiftUI updates affected views right away. If you
want to smooth visual transitions, you can tell SwiftUI to animate them by
wrapping the state change that triggers them in a call to the
`withAnimation(_:_:)` function. For example, you can animate changes
controlled by the `isPlaying` Boolean:

By changing `isPlaying` inside the animation function’s trailing closure, you
tell SwiftUI to animate anything that depends on the wrapped value, like a
scale effect on the button’s image:

SwiftUI transitions the scale effect input over time between the given values
of `1` and `1.5`, using the curve and duration that you specify, or reasonable
default values if you provide none. On the other hand, the image content isn’t
affected by the animation, even though the same Boolean dictates which system
image to display. That’s because SwiftUI can’t incrementally transition in a
meaningful way between the two strings `pause.circle` and `play.circle`.

You can add animation to a state property, or as in the above example, to a
binding. Either way, SwiftUI animates any view changes that happen when the
underlying stored value changes. For example, if you add a background color to
the `PlayerView` — at a level of view hierarchy above the location of the
animation block — SwiftUI animates that as well:

When you want to apply animations to specific views, rather than across all
views triggered by a change in state, use the `animation(_:value:)` view
modifier instead.

## See Also

### Creating and sharing view state

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# State

A property wrapper type that can read and write a value managed by SwiftUI.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct State<Value>

## Overview

Use state as the single source of truth for a given value type that you store
in a view hierarchy. Create a state value in an `App`, `Scene`, or `View` by
applying the `@State` attribute to a property declaration and providing an
initial value. Declare state as private to prevent setting it in a memberwise
initializer, which can conflict with the storage management that SwiftUI
provides:

SwiftUI manages the property’s storage. When the value changes, SwiftUI
updates the parts of the view hierarchy that depend on the value. To access a
state’s underlying value, you use its `wrappedValue` property. However, as a
shortcut Swift enables you to access the wrapped value by referring directly
to the state instance. The above example reads and writes the `isPlaying`
state property’s wrapped value by referring to the property directly.

Declare state as private in the highest view in the view hierarchy that needs
access to the value. Then share the state with any subviews that also need
access, either directly for read-only access, or as a binding for read-write
access. You can safely mutate state properties from any thread.

### Share state with subviews

If you pass a state property to a subview, SwiftUI updates the subview any
time the value changes in the container view, but the subview can’t modify the
value. To enable the subview to modify the state’s stored value, pass a
`Binding` instead.

For example, you can remove the `isPlaying` state from the play button in the
above example, and instead make the button take a binding:

Then you can define a player view that declares the state and creates a
binding to the state. Get the binding to the state value by accessing the
state’s `projectedValue`, which you get by prefixing the property name with a
dollar sign (`$`):

Like you do for a `StateObject`, declare `State` as private to prevent setting
it in a memberwise initializer, which can conflict with the storage management
that SwiftUI provides. Unlike a state object, always initialize state by
providing a default value in the state’s declaration, as in the above
examples. Use state only for storage that’s local to a view and its subviews.

### Store observable objects

You can also store observable objects that you create with the `Observable()`
macro in `State`; for example:

A `State` property always instantiates its default value when SwiftUI
instantiates the view. For this reason, avoid side effects and performance-
intensive work when initializing the default value. For example, if a view
updates frequently, allocating a new default object each time the view
initializes can become expensive. Instead, you can defer the creation of the
object using the `task(priority:_:)` modifier, which is called only once when
the view first appears:

Delaying the creation of the observable state object ensures that unnecessary
allocations of the object doesn’t happen each time SwiftUI initializes the
view. Using the `task(priority:_:)` modifier is also an effective way to defer
any other kind of work required to create the initial state of the view, such
as network calls or file access.

Note

It’s possible to store an object that conforms to the `ObservableObject`
protocol in a `State` property. However the view will only update when the
reference to the object changes, such as when setting the property with a
reference to another object. The view will not update if any of the object’s
published properties change. To track changes to both the reference and the
object’s published properties, use `StateObject` instead of `State` when
storing the object.

### Share observable state objects with subviews

To share an `Observable` object stored in `State` with a subview, pass the
object reference to the subview. SwiftUI updates the subview anytime an
observable property of the object changes, but only when the subview’s `body`
reads the property. For example, in the following code `BookView` updates each
time `title` changes but not when `isAvailable` changes:

`State` properties provide bindings to their value. When storing an object,
you can get a `Binding` to that object, specifically the reference to the
object. This is useful when you need to change the reference stored in state
in some other subview, such as setting the reference to `nil`:

However, passing a `Binding` to an object stored in `State` isn’t necessary
when you need to change properties of that object. For example, you can set
the properties of the object to new values in a subview by passing the object
reference instead of a binding to the reference:

If you need a binding to a specific property of the object, pass either the
binding to the object and extract bindings to specific properties where
needed, or pass the object reference and use the `Bindable` property wrapper
to create bindings to specific properties. For example, in the following code
`BookEditorView` wraps `book` with `@Bindable`. Then the view uses the `$`
syntax to pass to a `TextField` a binding to `title`:

## Topics

### Creating a state

`init(wrappedValue: Value)`

Creates a state property that stores an initial wrapped value.

`init(initialValue: Value)`

Creates a state property that stores an initial value.

`init()`

Creates a state property without an initial value.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the state variable.

`var projectedValue: Binding<Value>`

A binding to the state value.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# Bindable

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @propertyWrapper
    struct Bindable<Value>

## Overview

Use this property wrapper to create bindings to mutable properties of a data
model object that conforms to the `Observable` protocol. For example, the
following code wraps the `book` input with `@Bindable`. Then it uses a
`TextField` to change the `title` property of a book, and a `Toggle` to change
the `isAvailable` property, using the `$` syntax to pass a binding for each
property to those controls.

You can use the `Bindable` property wrapper on properties and variables to an
`Observable` object. This includes global variables, properties that exists
outside of SwiftUI types, or even local variables. For example, you can create
a `@Bindable` variable within a view’s `body`:

The `@Bindable` variable `book` provides a binding that connects `TextField`
to the `title` property of a book so that a person can make changes directly
to the model data.

Use this same approach when you need a binding to a property of an observable
object stored in a view’s environment. For example, the following code uses
the `Environment` property wrapper to retrieve an instance of the observable
type `Book`. Then the code creates a `@Bindable` variable `book` and passes a
binding for the `title` property to a `TextField` using the `$` syntax.

## Topics

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

## Relationships

### Conforms To

  * `Identifiable`
  * `Sendable`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# Binding

A property wrapper type that can read and write a value owned by a source of
truth.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper @dynamicMemberLookup
    struct Binding<Value>

## Overview

Use a binding to create a two-way connection between a property that stores
data, and a view that displays and changes the data. A binding connects a
property to a source of truth stored elsewhere, instead of storing data
directly. For example, a button that toggles between play and pause can create
a binding to a property of its parent view using the `Binding` property
wrapper.

The parent view declares a property to hold the playing state, using the
`State` property wrapper to indicate that this property is the value’s source
of truth.

When `PlayerView` initializes `PlayButton`, it passes a binding of its state
property into the button’s binding property. Applying the `$` prefix to a
property wrapped value returns its `projectedValue`, which for a state
property wrapper returns a binding to the value.

Whenever the user taps the `PlayButton`, the `PlayerView` updates its
`isPlaying` state.

Note

To create bindings to properties of a type that conforms to the `Observable`
protocol, use the `Bindable` property wrapper. For more information, see
Migrating from the Observable Object protocol to the Observable macro.

## Topics

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

### Default Implementations

API Reference

Identifiable Implementations

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `DynamicProperty`
  * `Identifiable`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

Macro

# Observable()

Defines and implements conformance of the Observable protocol.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @attached(member, names: named(_$observationRegistrar), named(access), named(withMutation)) @attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()

## Overview

This macro adds observation support to a custom type and conforms the type to
the `Observable` protocol. For example, the following code applies the
`Observable` macro to the type `Car` making it observable:

## See Also

### Observable conformance

`protocol Observable`

A type that emits notifications to observers when underlying data changes.

Structure

# StateObject

A property wrapper type that instantiates an observable object.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct StateObject<ObjectType> where ObjectType : ObservableObject

## Overview

Use a state object as the single source of truth for a reference type that you
store in a view hierarchy. Create a state object in an `App`, `Scene`, or
`View` by applying the `@StateObject` attribute to a property declaration and
providing an initial value that conforms to the `ObservableObject` protocol.
Declare state objects as private to prevent setting them from a memberwise
initializer, which can conflict with the storage management that SwiftUI
provides:

SwiftUI creates a new instance of the model object only once during the
lifetime of the container that declares the state object. For example, SwiftUI
doesn’t create a new instance if a view’s inputs change, but does create a new
instance if the identity of a view changes. When published properties of the
observable object change, SwiftUI updates any view that depends on those
properties, like the `Text` view in the above example.

Note

If you need to store a value type, like a structure, string, or integer, use
the `State` property wrapper instead. Also use `State` if you need to store a
reference type that conforms to the `Observable()` protocol. To learn more
about Observation in SwiftUI, see Managing model data in your app.

### Share state objects with subviews

You can pass a state object into a subview through a property that has the
`ObservedObject` attribute. Alternatively, add the object to the environment
of a view hierarchy by applying the `environmentObject(_:)` modifier to a
view, like `MySubView` in the above code. You can then read the object inside
`MySubView` or any of its descendants using the `EnvironmentObject` attribute:

Get a `Binding` to the state object’s properties using the dollar sign (`$`)
operator. Use a binding when you want to create a two-way connection. In the
above code, the `Toggle` controls the model’s `isEnabled` value through a
binding.

### Initialize state objects using external data

When a state object’s initial state depends on data that comes from outside
its container, you can call the object’s initializer explicitly from within
its container’s initializer. For example, suppose the data model from the
previous example takes a `name` input during initialization and you want to
use a value for that name that comes from outside the view. You can do this
with a call to the state object’s initializer inside an explicit initializer
that you create for the view:

Use caution when doing this. SwiftUI only initializes a state object the first
time you call its initializer in a given view. This ensures that the object
provides stable storage even as the view’s inputs change. However, it might
result in unexpected behavior or unwanted side effects if you explicitly
initialize the state object.

In the above example, if the `name` input to `MyInitializableView` changes,
SwiftUI reruns the view’s initializer with the new value. However, SwiftUI
runs the autoclosure that you provide to the state object’s initializer only
the first time you call the state object’s initializer, so the model’s stored
`name` value doesn’t change.

Explicit state object initialization works well when the external data that
the object depends on doesn’t change for a given instance of the object’s
container. For example, you can create two views with different constant
names:

Important

Even for a configurable state object, you still declare it as private. This
ensures that you can’t accidentally set the parameter through a memberwise
initializer of the view, because doing so can conflict with the framework’s
storage management and produce unexpected results.

### Force reinitialization by changing view identity

If you want SwiftUI to reinitialize a state object when a view input changes,
make sure that the view’s identity changes at the same time. One way to do
this is to bind the view’s identity to the value that changes using the
`id(_:)` modifier. For example, you can ensure that the identity of an
instance of `MyInitializableView` changes when its `name` input changes:

Note

If your view appears inside a `ForEach`, it implicitly receives an `id(_:)`
modifier that uses the identifier of the corresponding data element.

If you need the view to reinitialize state based on changes in more than one
value, you can combine the values into a single identifier using a `Hasher`.
For example, if you want to update the data model in `MyInitializableView`
when the values of either `name` or `isEnabled` change, you can combine both
variables into a single hash:

Then apply the combined hash to the view as an identifier:

Be mindful of the performance cost of reinitializing the state object every
time the input changes. Also, changing view identity can have side effects.
For example, SwiftUI doesn’t automatically animate changes inside the view if
the view’s identity changes at the same time. Also, changing the identity
resets _all_ state held by the view, including values that you manage as
`State`, `FocusState`, `GestureState`, and so on.

## Topics

### Creating a state object

`init(wrappedValue: () -> ObjectType)`

Creates a new state object with an initial wrapped value.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the state object.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the state object that creates bindings to its properties.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating model data

Managing model data in your app

Create connections between your app’s data model and views.

Migrating from the Observable Object protocol to the Observable macro

Update your existing app to leverage the benefits of Observation in Swift.

`macro Observable()`

Defines and implements conformance of the Observable protocol.

Monitoring data changes in your app

Show changes to data in your app’s user interface by using observable objects.

`struct ObservedObject`

A property wrapper type that subscribes to an observable object and
invalidates a view whenever the observable object changes.

`protocol ObservableObject`

A type of object with a publisher that emits before the object has changed.

Structure

# ObservedObject

A property wrapper type that subscribes to an observable object and
invalidates a view whenever the observable object changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct ObservedObject<ObjectType> where ObjectType : ObservableObject

## Overview

Add the `@ObservedObject` attribute to a parameter of a SwiftUI `View` when
the input is an `ObservableObject` and you want the view to update when the
object’s published properties change. You typically do this to pass a
`StateObject` into a subview.

The following example defines a data model as an observable object,
instantiates the model in a view as a state object, and then passes the
instance to a subview as an observed object:

When any published property of the observable object changes, SwiftUI updates
any view that depends on the object. Subviews can also make updates to the
model properties, like the `Toggle` in the above example, that propagate to
other observers throughout the view hierarchy.

Don’t specify a default or initial value for the observed object. Use the
attribute only for a property that acts as an input for a view, as in the
above example.

Note

Don’t wrap objects conforming to the `Observable` protocol with
`@ObservedObject`. SwiftUI automatically tracks dependencies to `Observable`
objects used within body and updates dependent views when their data changes.
Attempting to wrap an `Observable` object with `@ObservedObject` may cause a
compiler error, because it requires that its wrapped object to conform to the
`ObservableObject` protocol.

If the view needs a binding to a property of an `Observable` object in its
body, wrap the object with the `Bindable` property wrapper instead; for
example, `@Bindable var model: DataModel`. For more information, see Managing
model data in your app.

## Topics

### Creating an observed object

`init(wrappedValue: ObjectType)`

Creates an observed object with an initial wrapped value.

`init(initialValue: ObjectType)`

Creates an observed object with an initial value.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating model data

Managing model data in your app

Create connections between your app’s data model and views.

Migrating from the Observable Object protocol to the Observable macro

Update your existing app to leverage the benefits of Observation in Swift.

`macro Observable()`

Defines and implements conformance of the Observable protocol.

Monitoring data changes in your app

Show changes to data in your app’s user interface by using observable objects.

`struct StateObject`

A property wrapper type that instantiates an observable object.

`protocol ObservableObject`

A type of object with a publisher that emits before the object has changed.

Protocol

# ObservableObject

A type of object with a publisher that emits before the object has changed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ObservableObject : AnyObject

## Overview

By default an `ObservableObject` synthesizes an `objectWillChange` publisher
that emits the changed value before any of its `@Published` properties
changes.

## Topics

### Publishing Changes

`var objectWillChange: Self.ObjectWillChangePublisher`

A publisher that emits before the object has changed.

**Required** Default implementation provided.

`associatedtype ObjectWillChangePublisher : Publisher =
ObservableObjectPublisher`

The type of publisher that emits before the object has changed.

**Required**

## See Also

### Observable Objects

`class ObservableObjectPublisher`

A publisher that publishes changes from observable objects.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping () -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. In the following code example, `PlayerView` calls into its
model when `playState` changes model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping (V, V) -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

`oldValue`

    

The old value that failed the comparison check (or the initial value when
requested).

`newValue`

    

The new value that failed the comparison check.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. The old and new observed values are passed into the
closure. In the following code example, `PlayerView` passes both the old and
new values to the model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onReceive(_:perform:)

Adds an action to perform when this view detects data emitted by the given
publisher.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onReceive<P>(
        _ publisher: P,
        perform action: @escaping (P.Output) -> Void
    ) -> some View where P : Publisher, P.Failure == Never
    

##  Parameters

`publisher`

    

The publisher to subscribe to.

`action`

    

The action to perform when an event is emitted by `publisher`. The event
emitted by publisher is passed as a parameter to `action`.

## Return Value

A view that triggers `action` when `publisher` emits an event.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

Instance Method

# environmentObject(_:)

Supplies an observable object to a view’s hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The object to store and make available to the view’s hierarchy.

## Discussion

Use this modifier to add an observable object to a view’s environment. The
object must conform to the `ObservableObject` protocol.

Adding an object to a view’s environment makes the object available to
subviews in the view’s hierarchy. To retrieve the object in a subview, use the
`EnvironmentObject` property wrapper.

Note

If the observable object conforms to the `Observable` protocol, use either
`environment(_:)` or the `environment(_:_:)` modifier to add the object to the
view’s environment.

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Instance Method

# environmentObject(_:)

Supplies an `ObservableObject` to a view subhierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some Scene where T : ObservableObject
    

##  Parameters

`object`

    

the object to store and make available to the scene’s subhierarchy.

## Discussion

The object can be read by any child by using `EnvironmentObject`:

You then read the object inside `ContentView` or one of its descendants using
the `EnvironmentObject` property wrapper:

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Structure

# EnvironmentObject

A property wrapper type for an observable object that a parent or ancestor
view supplies.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject

## Overview

An environment object invalidates the current view whenever the observable
object that conforms to `ObservableObject` changes. If you declare a property
as an environment object, be sure to set a corresponding model object on an
ancestor view by calling its `environmentObject(_:)` modifier.

Note

If your observable object conforms to the `Observable` protocol, use
`Environment` instead of `EnvironmentObject` and set the model object in an
ancestor view by calling its `environment(_:)` or `environment(_:_:)`
modifiers.

## Topics

### Creating an environment object

`init()`

Creates an environment object.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the environment object.

`var projectedValue: EnvironmentObject<ObjectType>.Wrapper`

A projection of the environment object that creates bindings to its properties
using dynamic member lookup.

`struct Wrapper`

A wrapper of the underlying environment object that can create bindings to its
properties using dynamic member lookup.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

Protocol

# DynamicProperty

An interface for a stored variable that updates an external property of a
view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol DynamicProperty

## Overview

The view gives values to these properties prior to recomputing the view’s
`body`.

## Topics

### Updating the value

`func update()`

Updates the underlying value of the stored value.

**Required** Default implementation provided.

## Relationships

### Conforming Types

  * `AccessibilityFocusState`
  * `AppStorage`
  * `Binding`
  * `Environment`
  * `EnvironmentObject`
  * `FetchRequest`

Conforms when `Result` conforms to `NSFetchRequestResult`.

  * `FocusState`
  * `FocusedBinding`
  * `FocusedObject`
  * `FocusedValue`
  * `GestureState`
  * `NSApplicationDelegateAdaptor`
  * `Namespace`
  * `ObservedObject`
  * `PhysicalMetric`
  * `ScaledMetric`
  * `SceneStorage`
  * `SectionedFetchRequest`

Conforms when `SectionIdentifier` conforms to `Hashable` and `Result` conforms
to `NSFetchRequestResult`.

  * `State`
  * `StateObject`
  * `UIApplicationDelegateAdaptor`
  * `WKApplicationDelegateAdaptor`
  * `WKExtensionDelegateAdaptor`

