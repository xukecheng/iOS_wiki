Initializer

# init(wrappedValue:)

Creates an observed object with an initial wrapped value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(wrappedValue: ObjectType)

##  Parameters

`wrappedValue`

    

An initial value for the observable object.

## Discussion

Don’t call this initializer directly. Instead, declare an input to a view with
the `@ObservedObject` attribute, and pass a value to this input when you
instantiate the view. Unlike a `StateObject` which manages data storage, you
use an observed object to refer to storage that you manage elsewhere, as in
the following example:

Explicitly calling the observed object initializer in `MySubView` would behave
correctly, but would needlessly recreate the same observed object instance
every time SwiftUI calls the view’s initializer to redraw the view.

## See Also

### Creating an observed object

`init(initialValue: ObjectType)`

Creates an observed object with an initial value.

Initializer

# init(initialValue:)

Creates an observed object with an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(initialValue: ObjectType)

##  Parameters

`initialValue`

    

An initial value.

## Discussion

This initializer has the same behavior as the `init(wrappedValue:)`
initializer. See that initializer for more information.

## See Also

### Creating an observed object

`init(wrappedValue: ObjectType)`

Creates an observed object with an initial wrapped value.

Instance Property

# wrappedValue

The underlying value that the observed object references.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType

## Discussion

The wrapped value property provides primary access to the observed object’s
data. However, you don’t typically access it by name. Instead, SwiftUI
accesses this property for you when you refer to the variable that you create
with the `@ObservedObject` attribute.

When you change a wrapped value, you can access the new value immediately.
However, SwiftUI updates views that display the value asynchronously, so the
interface might not update immediately.

## See Also

### Getting the value

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

Instance Property

# projectedValue

A projection of the observed object that creates bindings to its properties.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<ObjectType>.Wrapper { get }

## Discussion

Use the projected value to get a `Binding` to a property of an observed
object. To access the projected value, prefix the property variable with a
dollar sign (`$`). For example, you can get a binding to a model’s `isEnabled`
Boolean so that a `Toggle` can control its value:

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

Structure

# ObservedObject.Wrapper

A wrapper of the underlying observable object that can create bindings to its
properties.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @frozen
    struct Wrapper

## Topics

### Subscripts

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<ObjectType,
Subject>) -> Binding<Subject>`

Gets a binding to the value of a specified key path.

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.

