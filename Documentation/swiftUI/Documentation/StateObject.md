Initializer

# init(wrappedValue:)

Creates a new state object with an initial wrapped value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(wrappedValue thunk: @autoclosure @escaping () -> ObjectType)

##  Parameters

`thunk`

    

An initial value for the state object.

## Discussion

You typically don’t call this initializer directly. Instead, SwiftUI calls it
for you when you declare a property with the `@StateObject` attribute in an
`App`, `Scene`, or `View` and provide an initial value:

SwiftUI creates only one instance of the state object for each container
instance that you declare. In the above code, SwiftUI creates `model` only the
first time it initializes a particular instance of `MyView`. On the other
hand, each instance of `MyView` creates a distinct instance of the data model.
For example, each of the views in the following `VStack` has its own model
storage:

### Initialize using external data

If the initial state of a state object depends on external data, you can call
this initializer directly. However, use caution when doing this, because
SwiftUI only initializes the object once during the lifetime of the view —
even if you call the state object initializer more than once — which might
result in unexpected behavior. For more information and an example, see
`StateObject`.

Instance Property

# wrappedValue

The underlying value referenced by the state object.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType { get }

## Discussion

The wrapped value property provides primary access to the value’s data.
However, you don’t typically access it directly. Instead, SwiftUI accesses
this property for you when you refer to the variable that you create with the
`@StateObject` attribute:

When you change a wrapped value, you can access the new value immediately.
However, SwiftUI updates views that display the value asynchronously, so the
interface might not update immediately.

## See Also

### Getting the value

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the state object that creates bindings to its properties.

Instance Property

# projectedValue

A projection of the state object that creates bindings to its properties.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<ObjectType>.Wrapper { get }

## Discussion

Use the projected value to get a `Binding` to a property of a state object. To
access the projected value, prefix the property name with a dollar sign (`$`).
For example, you can get a binding to a model’s `isEnabled` Boolean so that a
`Toggle` can control the value:

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the state object.

