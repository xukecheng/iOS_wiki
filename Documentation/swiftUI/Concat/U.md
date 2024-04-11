# UIApplicationDelegateAdaptor

Initializer

# init(_:)

Creates a UIKit app delegate adaptor.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` protocol.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling upon it to
handle application delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the `Environment`,
make sure the delegate class also conforms to the `ObservableObject` protocol.
That causes SwiftUI to invoke the `init(_:)` initializer rather than this one.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

Initializer

# init(_:)

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` and `ObservableObject` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`ObservableObject` protocol. In this case, SwiftUI automatically places the
delegate in the `Environment`. You can access such a delegate from any scene
or view in your app using the `EnvironmentObject` property wrapper:

If your delegate isn’t an observable object, SwiftUI invokes the `init(_:)`
initializer rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

Initializer

# init(_:)

Creates a UIKit app delegate adaptor using an observable delegate.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` and `Observable` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`Observable` protocol. In this case, SwiftUI automatically places the delegate
in the `Environment`. You can access such a delegate from any scene or view in
your app using the `Environment` property wrapper:

If your delegate isn’t observable, SwiftUI invokes the `init(_:)` initializer
rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

Instance Property

# projectedValue

A projection of the observed object that provides bindings to its properties.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

## Discussion

Use the projected value to get a binding to a value that the delegate
publishes. Access the projected value by prefixing the name of the delegate
instance with a dollar sign (`$`). For example, you might publish a Boolean
value in your application delegate:

If you declare the delegate in your `App` using the
`UIApplicationDelegateAdaptor` property wrapper, you can get the delegate that
SwiftUI instantiates from the environment and access a binding to its
published values from any view in your app:

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying app delegate.

Instance Property

# wrappedValue

The underlying app delegate.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.



# UIViewRepresentable

Instance Method

# makeUIView(context:)

Creates the view object and configures its initial state.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeUIView(context: Self.Context) -> Self.UIViewType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your UIKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object.
Configure the view using your app’s current data and contents of the `context`
parameter. The system calls this method only once, when it creates your view
for the first time. For all subsequent updates, the system calls the
`updateUIView(_:context:)` method.

## See Also

### Creating and updating the view

`func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Instance Method

# updateUIView(_:context:)

Updates the state of the specified view with new information from SwiftUI.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func updateUIView(
        _ uiView: Self.UIViewType,
        context: Self.Context
    )

**Required**

##  Parameters

`uiView`

    

Your custom view object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding UIKit view. Use this method to update the
configuration of your view to match the new state information provided in the
`context` parameter.

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Type Alias

# UIViewRepresentable.Context

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    typealias Context = UIViewRepresentableContext<Self>

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` associatedtype UIViewType : UIView`

The type of view to present.

**Required**

Associated Type

# UIViewType

The type of view to present.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype UIViewType : UIView

**Required**

## See Also

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

Instance Method

# sizeThatFits(_:uiView:context:)

Given a proposed size, returns the preferred size of the composite view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    @MainActor
    func sizeThatFits(
        _ proposal: ProposedViewSize,
        uiView: Self.UIViewType,
        context: Self.Context
    ) -> CGSize?

**Required** Default implementation provided.

##  Parameters

`proposal`

    

The proposed size for the view.

`uiView`

    

Your custom view object.

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

The composite size of the represented view controller. Returning a value of
`nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during
the same layout pass. SwiftUI views choose their own size, so one of the
values returned from this function will always be used as the actual size of
the composite view.

## Default Implementations

### UIViewRepresentable Implementations

`func sizeThatFits(ProposedViewSize, uiView: Self.UIViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

Type Method

# dismantleUIView(_:coordinator:)

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    static func dismantleUIView(
        _ uiView: Self.UIViewType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`uiView`

    

Your custom view object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
view. For example, you might use this method to remove observers or update
other parts of your SwiftUI interface.

## Default Implementations

### UIViewRepresentable Implementations

`static func dismantleUIView(Self.UIViewType, coordinator: Self.Coordinator)`

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your view might affect other parts of your
app. In your implementation, create a custom Swift instance that can
communicate with other parts of your interface. For example, you might provide
an instance that binds its variables to SwiftUI properties, causing the two to
remain synchronized. If your view doesn’t interact with other parts of your
app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeUIView(context:)` method.
The system provides your coordinator either directly or as part of a context
structure when calling the other methods of your representable instance.

## Default Implementations

### UIViewRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the view.

**Required**

Associated Type

# Coordinator

A type to coordinate with the view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

**Required** Default implementation provided.

Type Alias

# UIViewRepresentable.LayoutOptions

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    typealias LayoutOptions



# UITraitBridgedEnvironmentKey

Type Method

# read(from:)

Reads the trait value from the trait collection, and returns the equivalent
environment value.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static func read(from traitCollection: UITraitCollection) -> Self.Value

**Required**

##  Parameters

`traitCollection`

    

The trait collection to read from.

## See Also

### Managing the keys

`static func write(to: inout any UIMutableTraits, value: Self.Value)`

**Required**

Type Method

# write(to:value:)

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static func write(
        to mutableTraits: inout any UIMutableTraits,
        value: Self.Value
    )

**Required**

## See Also

### Managing the keys

`static func read(from: UITraitCollection) -> Self.Value`

Reads the trait value from the trait collection, and returns the equivalent
environment value.

**Required**



# UserInterfaceSizeClass

Case

# UserInterfaceSizeClass.compact

The compact size class.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case compact

## See Also

### Getting size classes

`case regular`

The regular size class.

Case

# UserInterfaceSizeClass.regular

The regular size class.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case regular

## See Also

### Getting size classes

`case compact`

The compact size class.

Initializer

# init(_:)

Creates a SwiftUI size class from the specified UIKit size class.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init?(_ uiUserInterfaceSizeClass: UIUserInterfaceSizeClass)



# UnitPoint3D

Type Property

# origin

The origin of a view.

visionOS 1.0+

    
    
    static let origin: UnitPoint3D

## Discussion

A view’s origin appears in the top-left-back corner in a left-to-right
language environment, with positive x toward the right. It appears in the top-
right-back corner in a right-to-left language, with positive x toward the
left. Positive y is always toward the bottom of the view, and positive z
points toward the front.

## See Also

### Getting the origin

`static let zero: UnitPoint3D`

A 3D unit point with all components equal to zero.

Type Property

# zero

A 3D unit point with all components equal to zero.

visionOS 1.0+

    
    
    static let zero: UnitPoint3D

## Discussion

This point is equivalent to the `origin`. A view’s origin appears in the top-
left-back corner in a left-to-right language environment, with positive x
toward the right. It appears in the top-right-back corner in a right-to-left
language, with positive x toward the left. Positive y is always toward the
bottom of the view, and positive z points toward the front.

## See Also

### Getting the origin

`static let origin: UnitPoint3D`

The origin of a view.

Type Property

# topLeadingBack

A point that’s in the top-leading-back corner of a view.

visionOS 1.0+

    
    
    static let topLeadingBack: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting top points

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topLeading

A point that’s centered in the depth dimension on the top-leading edge of a
view.

visionOS 1.0+

    
    
    static let topLeading: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topLeadingFront

A point that’s in the top-leading-front corner of a view.

visionOS 1.0+

    
    
    static let topLeadingFront: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topBack

A point that’s centered horizontally on the top-back edge of a view.

visionOS 1.0+

    
    
    static let topBack: UnitPoint3D

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# top

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

visionOS 1.0+

    
    
    static let top: UnitPoint3D

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topFront

A point that’s centered horizontally on the top-front edge of a view.

visionOS 1.0+

    
    
    static let topFront: UnitPoint3D

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topTrailingBack

A point that’s in the top-trailing-back corner of a view.

visionOS 1.0+

    
    
    static let topTrailingBack: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topTrailing

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

visionOS 1.0+

    
    
    static let topTrailing: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

Type Property

# topTrailingFront

A point that’s in the top-trailing-front corner of a view.

visionOS 1.0+

    
    
    static let topTrailingFront: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

Type Property

# leadingBack

A point that’s centered vertically on the leading-back edge of a view.

visionOS 1.0+

    
    
    static let leadingBack: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting middle points

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# leading

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

visionOS 1.0+

    
    
    static let leading: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# leadingFront

A point that’s centered vertically on the leading-front edge of a view.

visionOS 1.0+

    
    
    static let leadingFront: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# back

A point that’s centered horizontally and vertically on the back face of a
view.

visionOS 1.0+

    
    
    static let back: UnitPoint3D

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# center

A point that’s centered in a view.

visionOS 1.0+

    
    
    static let center: UnitPoint3D

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# front

A point that’s centered horizontally and vertically on the front face of a
view.

visionOS 1.0+

    
    
    static let front: UnitPoint3D

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# trailingBack

A point that’s centered vertically on the trailing-back edge of a view.

visionOS 1.0+

    
    
    static let trailingBack: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# trailing

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

visionOS 1.0+

    
    
    static let trailing: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

Type Property

# trailingFront

A point that’s centered vertically on the trailing-front edge of a view.

visionOS 1.0+

    
    
    static let trailingFront: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

Type Property

# bottomLeadingBack

A point that’s in the bottom-leading-back corner of a view.

visionOS 1.0+

    
    
    static let bottomLeadingBack: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomLeading

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

visionOS 1.0+

    
    
    static let bottomLeading: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomLeadingFront

A point that’s in the bottom-leading-front corner of a view.

visionOS 1.0+

    
    
    static let bottomLeadingFront: UnitPoint3D

## Discussion

The leading edge appears on the left in a left-to-right language environment
and on the right in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomBack

A point that’s centered horizontally on the bottom-back edge of a view.

visionOS 1.0+

    
    
    static let bottomBack: UnitPoint3D

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottom

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

visionOS 1.0+

    
    
    static let bottom: UnitPoint3D

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomFront

A point that’s centered horizontally on the bottom-front edge of a view.

visionOS 1.0+

    
    
    static let bottomFront: UnitPoint3D

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomTrailingBack

A point that’s in the bottom-trailing-back corner of a view.

visionOS 1.0+

    
    
    static let bottomTrailingBack: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomTrailing

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

visionOS 1.0+

    
    
    static let bottomTrailing: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

Type Property

# bottomTrailingFront

A point that’s in the bottom-trailing-front corner of a view.

visionOS 1.0+

    
    
    static let bottomTrailingFront: UnitPoint3D

## Discussion

The trailing edge appears on the right in a left-to-right language environment
and on the left in a right-to-left environment.

## See Also

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

Initializer

# init()

Creates a 3D unit point at the origin.

visionOS 1.0+

    
    
    init()

## Discussion

A view’s origin appears in the top-left-back corner in a left-to-right
language environment, with positive x toward the right. It appears in the top-
right-back corner in a right-to-left language, with positive x toward the
left. Positive y is always toward the bottom of the view, and positive z
points toward the front.

## See Also

### Creating a point

`init(x: CGFloat, y: CGFloat, z: CGFloat)`

Creates a 3D unit point with the specified offsets.

Initializer

# init(x:y:z:)

Creates a 3D unit point with the specified offsets.

visionOS 1.0+

    
    
    init(
        x: CGFloat,
        y: CGFloat,
        z: CGFloat
    )

##  Parameters

`x`

    

The normalized distance from the origin to the point in the horizontal
dimension.

`y`

    

The normalized distance from the origin to the point in the vertical
dimension.

`z`

    

The normalized distance from the origin to the point in the depth dimension.

## Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## See Also

### Creating a point

`init()`

Creates a 3D unit point at the origin.

Instance Property

# x

The normalized distance from the origin to the point in the horizontal
direction.

visionOS 1.0+

    
    
    var x: CGFloat

## See Also

### Getting the point’s coordinates

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

`var z: CGFloat`

The normalized distance from the origin to the point in the depth dimension.

Instance Property

# y

The normalized distance from the origin to the point in the vertical
dimension.

visionOS 1.0+

    
    
    var y: CGFloat

## See Also

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var z: CGFloat`

The normalized distance from the origin to the point in the depth dimension.

Instance Property

# z

The normalized distance from the origin to the point in the depth dimension.

visionOS 1.0+

    
    
    var z: CGFloat

## See Also

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.



# UnifiedCompactWindowToolbarStyle

Initializer

# init()

Creates a unified compact window toolbar style.

macOS 11.0+

    
    
    init()

## See Also

### Creating the window toolbar style

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

Initializer

# init(showsTitle:)

Creates a unified compact window toolbar style.

macOS 11.0+

    
    
    init(showsTitle: Bool)

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.

Initializer

# init()

Creates a unified compact window toolbar style.

macOS 11.0+

    
    
    init()

## See Also

### Creating the window toolbar style

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

Initializer

# init(showsTitle:)

Creates a unified compact window toolbar style.

macOS 11.0+

    
    
    init(showsTitle: Bool)

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.



# UIViewControllerRepresentable

Instance Method

# makeUIViewController(context:)

Creates the view controller object and configures its initial state.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your UIKit view controller configured with the provided information.

## Discussion

You must implement this method and use it to create your view controller
object. Create the view controller using your app’s current data and contents
of the `context` parameter. The system calls this method only once, when it
creates your view controller for the first time. For all subsequent updates,
the system calls the `updateUIViewController(_:context:)` method.

## See Also

### Creating and updating the view controller

`func updateUIViewController(Self.UIViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewControllerType : UIViewController`

The type of view controller to present.

**Required**

Instance Method

# updateUIViewController(_:context:)

Updates the state of the specified view controller with new information from
SwiftUI.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func updateUIViewController(
        _ uiViewController: Self.UIViewControllerType,
        context: Self.Context
    )

**Required**

##  Parameters

`uiViewController`

    

Your custom view controller object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding UIKit view controller. Use this method to update
the configuration of your view controller to match the new state information
provided in the `context` parameter.

## See Also

### Creating and updating the view controller

`func makeUIViewController(context: Self.Context) ->
Self.UIViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` typealias Context`

`associatedtype UIViewControllerType : UIViewController`

The type of view controller to present.

**Required**

Type Alias

# UIViewControllerRepresentable.Context

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    typealias Context = UIViewControllerRepresentableContext<Self>

## See Also

### Creating and updating the view controller

`func makeUIViewController(context: Self.Context) ->
Self.UIViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateUIViewController(Self.UIViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` associatedtype UIViewControllerType : UIViewController`

The type of view controller to present.

**Required**

Associated Type

# UIViewControllerType

The type of view controller to present.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype UIViewControllerType : UIViewController

**Required**

## See Also

### Creating and updating the view controller

`func makeUIViewController(context: Self.Context) ->
Self.UIViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateUIViewController(Self.UIViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

Instance Method

# sizeThatFits(_:uiViewController:context:)

Given a proposed size, returns the preferred size of the composite view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    @MainActor
    func sizeThatFits(
        _ proposal: ProposedViewSize,
        uiViewController: Self.UIViewControllerType,
        context: Self.Context
    ) -> CGSize?

**Required** Default implementation provided.

##  Parameters

`proposal`

    

The proposed size for the view controller.

`uiViewController`

    

Your custom view controller object.

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

The composite size of the represented view controller. Returning a value of
`nil` indicates that the system should use the default sizing algorithm.

## Discussion

This method may be called more than once with different proposed sizes during
the same layout pass. SwiftUI views choose their own size, so one of the
values returned from this function will always be used as the actual size of
the composite view.

## Default Implementations

### UIViewControllerRepresentable Implementations

`func sizeThatFits(ProposedViewSize, uiViewController:
Self.UIViewControllerType, context: Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

Type Method

# dismantleUIViewController(_:coordinator:)

Cleans up the presented view controller (and coordinator) in anticipation of
their removal.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    static func dismantleUIViewController(
        _ uiViewController: Self.UIViewControllerType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`uiViewController`

    

Your custom view controller object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
view controller. For example, you might use this method to remove observers or
update other parts of your SwiftUI interface.

## Default Implementations

### UIViewControllerRepresentable Implementations

`static func dismantleUIViewController(Self.UIViewControllerType, coordinator:
Self.Coordinator)`

Cleans up the presented view controller (and coordinator) in anticipation of
their removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your view controller might affect other
parts of your app. In your implementation, create a custom Swift instance that
can communicate with other parts of your interface. For example, you might
provide an instance that binds its variables to SwiftUI properties, causing
the two to remain synchronized. If your view controller doesn’t interact with
other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeUIViewController(context:)`
method. The system provides your coordinator either directly or as part of a
context structure when calling the other methods of your representable
instance.

## Default Implementations

### UIViewControllerRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the view controller.

**Required**

Associated Type

# Coordinator

A type to coordinate with the view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

**Required** Default implementation provided.

Type Alias

# UIViewControllerRepresentable.LayoutOptions

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    typealias LayoutOptions



# UIViewRepresentableContext

Instance Property

# coordinator

The view’s associated coordinator.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    let coordinator: Representable.Coordinator

## See Also

### Coordinating view-related interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating view-related interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

Instance Property

# environment

The current environment.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your view when creating
or updating it.



# UIHostingOrnament

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this ornament.

visionOS 1.0+

    
    
    var rootView: Content { get set }

Instance Property

# contentAlignment

The alignment in the ornament used to position it.

visionOS 1.0+

    
    
    var contentAlignment: Alignment { get set }

Initializer

# init(sceneAnchor:contentAlignment:content:)

Creates an ornament with the specified alignment and content.

visionOS 1.0+

    
    
    init(
        sceneAnchor: UnitPoint,
        contentAlignment: Alignment = .center,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`sceneAnchor`

    

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

`contentAlignment`

    

The alignment in the ornament used to position it.

`content`

    

The content of the ornament.

Instance Property

# sceneAnchor

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

visionOS 1.0+

    
    
    var sceneAnchor: UnitPoint { get set }



# UnevenRoundedRectangle

Initializer

# init(cornerRadii:style:)

Creates a new rounded rectangle shape with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerRadii`

    

the radii of each corner.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating an uneven rounded rectangle

`init(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat,
bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style:
RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

Initializer

#
init(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)

Creates a new rounded rectangle shape with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        topLeadingRadius: CGFloat = 0,
        bottomLeadingRadius: CGFloat = 0,
        bottomTrailingRadius: CGFloat = 0,
        topTrailingRadius: CGFloat = 0,
        style: RoundedCornerStyle = .continuous
    )

## See Also

### Creating an uneven rounded rectangle

`init(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

Instance Property

# cornerRadii

The radii of each corner of the rounded rectangle.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var cornerRadii: RectangleCornerRadii

## See Also

### Getting the shape’s characteristics

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

Instance Property

# style

The style of corners drawn by the rounded rectangle.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var style: RoundedCornerStyle

## See Also

### Getting the shape’s characteristics

`var cornerRadii: RectangleCornerRadii`

The radii of each corner of the rounded rectangle.

Instance Property

# animatableData

The data to animate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var animatableData: RectangleCornerRadii.AnimatableData { get set }



# UIHostingConfiguration

Initializer

# init(content:)

Creates a hosting configuration with the given contents.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Content` conforms to `View` and `Background` is `EmptyView`.

##  Parameters

`content`

    

The contents of the SwiftUI hierarchy to be shown inside the cell.

Instance Method

# background(_:)

Sets the background contents for the hosting configuration’s enclosing cell.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func background<S>(_ style: S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>> where S : ShapeStyle

##  Parameters

`style`

    

The shape style to be used as the background of the cell.

## Discussion

The following example sets a custom view to the background of the cell:

## See Also

### Setting the background

`func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>`

Sets the background contents for the hosting configuration’s enclosing cell.

Instance Method

# background(content:)

Sets the background contents for the hosting configuration’s enclosing cell.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func background<B>(@ViewBuilder content: () -> B) -> UIHostingConfiguration<Content, B> where B : View

##  Parameters

`background`

    

The contents of the SwiftUI hierarchy to be shown inside the background of the
cell.

## Discussion

The following example sets a custom view to the background of the cell:

## See Also

### Setting the background

`func background<S>(S) -> UIHostingConfiguration<Content,
_UIHostingConfigurationBackgroundView<S>>`

Sets the background contents for the hosting configuration’s enclosing cell.

Instance Method

# margins(_:_:)

Sets the margins around the content of the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func margins(
        _ edges: Edge.Set = .all,
        _ insets: EdgeInsets
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`edges`

    

The edges to apply the insets. Any edges not specified will use the system
default values. The default value is `all`.

`insets`

    

The insets to apply.

## Discussion

Use this modifier to replace the default margins applied to the root of the
configuration. The following example creates 10 points of space between the
content and the background on the leading edge and 20 points of space on the
trailing edge:

## See Also

### Setting margins

`func margins(Edge.Set, CGFloat) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

Instance Method

# margins(_:_:)

Sets the margins around the content of the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func margins(
        _ edges: Edge.Set = .all,
        _ length: CGFloat
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`edges`

    

The edges to apply the insets. Any edges not specified will use the system
default values. The default value is `all`.

`length`

    

The amount to apply.

## Discussion

Use this modifier to replace the default margins applied to the root of the
configuration. The following example creates 20 points of space between the
content and the background on the horizontal edges.

## See Also

### Setting margins

`func margins(Edge.Set, EdgeInsets) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

Instance Method

# minSize(width:height:)

Sets the minimum size for the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func minSize(
        width: CGFloat? = nil,
        height: CGFloat? = nil
    ) -> UIHostingConfiguration<Content, Background>

##  Parameters

`width`

    

The value to use for the width dimension. A value of `nil` indicates that the
system default should be used.

`height`

    

The value to use for the height dimension. A value of `nil` indicates that the
system default should be used.

## Discussion

Use this modifier to indicate that a configuration’s associated cell can be
resized to a specific minimum. The following example allows the cell to be
compressed to zero size:

## See Also

### Setting a size

`func minSize() -> UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

Deprecated

Instance Method

# minSize()

Sets the minimum size for the configuration.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    func minSize() -> UIHostingConfiguration<Content, Background>

Deprecated

Use `minSize(width:height:)` instead.

## See Also

### Setting a size

`func minSize(width: CGFloat?, height: CGFloat?) ->
UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.



# UnitCurve

Type Property

# linear

A linear curve.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let linear: UnitCurve

## Discussion

As the linear curve is a straight line from (0, 0) to (1, 1), the output
progress is always equal to the input progress, and the velocity is always
equal to 1.0.

Type Property

# easeIn

A bezier curve that starts out slowly, then speeds up as it finishes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeIn: UnitCurve

## Discussion

The start and end control points are located at (x: 0.42, y: 0) and (x: 1, y:
1).

## See Also

### Getting easing curves

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# easeOut

A bezier curve that starts out quickly, then slows down as it approaches the
end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeOut: UnitCurve

## Discussion

The start and end control points are located at (x: 0, y: 0) and (x: 0.58, y:
1).

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# easeInOut

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeInOut: UnitCurve

## Discussion

The start and end control points are located at (x: 0.42, y: 0) and (x: 0.58,
y: 1).

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseIn

A curve that starts out slowly, then speeds up as it finishes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseIn: UnitCurve

## Discussion

The shape of the curve is equal to the fourth (bottom right) quadrant of a
unit circle.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseOut

A circular curve that starts out quickly, then slows down as it approaches the
end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseOut: UnitCurve

## Discussion

The shape of the curve is equal to the second (top left) quadrant of a unit
circle.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseInOut

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseInOut: UnitCurve

## Discussion

The shape of the curve is defined by a piecewise combination of
`circularEaseIn` and `circularEaseOut`.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

Type Method

# bezier(startControlPoint:endControlPoint:)

Creates a new curve using bezier control points.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func bezier(
        startControlPoint: UnitPoint,
        endControlPoint: UnitPoint
    ) -> UnitCurve

##  Parameters

`startControlPoint`

    

The cubic Bézier control point associated with the curve’s start point at (0,
0). The tangent vector from the start point to its control point defines the
initial velocity of the timing function.

`endControlPoint`

    

The cubic Bézier control point associated with the curve’s end point at (1,
1). The tangent vector from the end point to its control point defines the
final velocity of the timing function.

## Discussion

The x components of the control points are clamped to the range [0,1] when the
curve is evaluated.

Instance Property

# inverse

Returns a copy of the curve with its x and y components swapped.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var inverse: UnitCurve { get }

## Discussion

The inverse can be used to solve a curve in reverse: given a known output (y)
value, the corresponding input (x) value can be found by using `inverse`:

Instance Method

# value(at:)

Returns the output value (y component) of the curve at the given time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value(at progress: Double) -> Double

##  Parameters

`time`

    

The input progress (x component). The provided value is clamped to the range
[0,1].

## Return Value

The output value (y component) of the curve at the given progress.

## See Also

### Getting curve characteristics

`func velocity(at: Double) -> Double`

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

Instance Method

# velocity(at:)

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity(at progress: Double) -> Double

##  Parameters

`progress`

    

The input progress (x component). The provided value is clamped to the range
[0,1].

## Return Value

The velocity of the output value (y component) of the curve at the given time.

## See Also

### Getting curve characteristics

`func value(at: Double) -> Double`

Returns the output value (y component) of the curve at the given time.

Type Property

# easeInEaseOut

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeInEaseOut: UnitCurve

Deprecated

Use `easeInOut` instead.



# UnitPoint

Type Property

# zero

The origin of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let zero: UnitPoint

## Discussion

A view’s origin appears in the top-left corner in a left-to-right language
environment, with positive x toward the right. It appears in the top-right
corner in a right-to-left language, with positive x toward the left. Positive
y is always toward the bottom of the view.

Type Property

# topLeading

A point that’s in the top, leading corner of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let topLeading: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `topLeading` alignment. The leading edge appears on the
left in a left-to-right language environment and on the right in a right-to-
left environment.

## See Also

### Getting top points

`static let top: UnitPoint`

A point that’s centered horizontally on the top edge of a view.

`static let topTrailing: UnitPoint`

A point that’s in the top, trailing corner of a view.

Type Property

# top

A point that’s centered horizontally on the top edge of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let top: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `top` alignment.

## See Also

### Getting top points

`static let topLeading: UnitPoint`

A point that’s in the top, leading corner of a view.

`static let topTrailing: UnitPoint`

A point that’s in the top, trailing corner of a view.

Type Property

# topTrailing

A point that’s in the top, trailing corner of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let topTrailing: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `topTrailing` alignment. The trailing edge appears on the
right in a left-to-right language environment and on the left in a right-to-
left environment.

## See Also

### Getting top points

`static let topLeading: UnitPoint`

A point that’s in the top, leading corner of a view.

`static let top: UnitPoint`

A point that’s centered horizontally on the top edge of a view.

Type Property

# leading

A point that’s centered vertically on the leading edge of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let leading: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `leading` alignment. The leading edge appears on the left
in a left-to-right language environment and on the right in a right-to-left
environment.

## See Also

### Getting middle points

`static let center: UnitPoint`

A point that’s centered in a view.

`static let trailing: UnitPoint`

A point that’s centered vertically on the trailing edge of a view.

Type Property

# center

A point that’s centered in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let center: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `center` alignment.

## See Also

### Getting middle points

`static let leading: UnitPoint`

A point that’s centered vertically on the leading edge of a view.

`static let trailing: UnitPoint`

A point that’s centered vertically on the trailing edge of a view.

Type Property

# trailing

A point that’s centered vertically on the trailing edge of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let trailing: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `trailing` alignment. The trailing edge appears on the
right in a left-to-right language environment and on the left in a right-to-
left environment.

## See Also

### Getting middle points

`static let leading: UnitPoint`

A point that’s centered vertically on the leading edge of a view.

`static let center: UnitPoint`

A point that’s centered in a view.

Type Property

# bottomLeading

A point that’s in the bottom, leading corner of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottomLeading: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `bottomLeading` alignment. The leading edge appears on
the left in a left-to-right language environment and on the right in a right-
to-left environment.

## See Also

### Getting bottom points

`static let bottom: UnitPoint`

A point that’s centered horizontally on the bottom edge of a view.

`static let bottomTrailing: UnitPoint`

A point that’s in the bottom, trailing corner of a view.

Type Property

# bottom

A point that’s centered horizontally on the bottom edge of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottom: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `bottom` alignment.

## See Also

### Getting bottom points

`static let bottomLeading: UnitPoint`

A point that’s in the bottom, leading corner of a view.

`static let bottomTrailing: UnitPoint`

A point that’s in the bottom, trailing corner of a view.

Type Property

# bottomTrailing

A point that’s in the bottom, trailing corner of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottomTrailing: UnitPoint

## Discussion

This point occupies the position where the horizontal and vertical alignment
guides intersect for `bottomTrailing` alignment. The trailing edge appears on
the right in a left-to-right language environment and on the left in a right-
to-left environment.

## See Also

### Getting bottom points

`static let bottomLeading: UnitPoint`

A point that’s in the bottom, leading corner of a view.

`static let bottom: UnitPoint`

A point that’s centered horizontally on the bottom edge of a view.

Initializer

# init()

Creates a unit point at the origin.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## Discussion

A view’s origin appears in the top-left corner in a left-to-right language
environment, with positive x toward the right. It appears in the top-right
corner in a right-to-left language, with positive x toward the left. Positive
y is always toward the bottom of the view.

## See Also

### Creating a point

`init(x: CGFloat, y: CGFloat)`

Creates a unit point with the specified horizontal and vertical offsets.

Initializer

# init(x:y:)

Creates a unit point with the specified horizontal and vertical offsets.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        x: CGFloat,
        y: CGFloat
    )

##  Parameters

`x`

    

The normalized distance from the origin to the point in the horizontal
direction.

`y`

    

The normalized distance from the origin to the point in the vertical
direction.

## Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## See Also

### Creating a point

`init()`

Creates a unit point at the origin.

Instance Property

# x

The normalized distance from the origin to the point in the horizontal
direction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var x: CGFloat

## See Also

### Getting the point’s coordinates

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

Instance Property

# y

The normalized distance from the origin to the point in the vertical
dimension.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var y: CGFloat

## See Also

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.



# UIHostingControllerSizingOptions

Type Property

# intrinsicContentSize

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static let intrinsicContentSize: UIHostingControllerSizingOptions

## Discussion

Use this option when the hosting controller’s view is being laid out with Auto
Layout.

Note

This option comes with a performance cost because it asks for the ideal size
of the content using the `unspecified` size proposal.

## See Also

### Getting sizing options

`static let preferredContentSize: UIHostingControllerSizingOptions`

The hosting controller tracks its content’s ideal size in its preferred
content size.

Type Property

# preferredContentSize

The hosting controller tracks its content’s ideal size in its preferred
content size.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static let preferredContentSize: UIHostingControllerSizingOptions

## Discussion

Use this option when using a hosting controller with a container view
controller that requires up-to-date knowledge of the hosting controller’s
ideal size.

Note

This option comes with a performance cost because it asks for the ideal size
of the content using the `unspecified` size proposal.

## See Also

### Getting sizing options

`static let intrinsicContentSize: UIHostingControllerSizingOptions`

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

Initializer

# init(rawValue:)

Creates a new option set from a raw value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init(rawValue: Int)

## See Also

### Creating a sizing option

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    let rawValue: Int

## See Also

### Creating a sizing option

`init(rawValue: Int)`

Creates a new option set from a raw value.



# UnifiedWindowToolbarStyle

Initializer

# init()

Creates a unified window toolbar style.

macOS 11.0+

    
    
    init()

## See Also

### Creating the window toolbar style

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

Initializer

# init(showsTitle:)

Creates a unified window toolbar style.

macOS 11.0+

    
    
    init(showsTitle: Bool)

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.

Initializer

# init()

Creates a unified window toolbar style.

macOS 11.0+

    
    
    init()

## See Also

### Creating the window toolbar style

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

Initializer

# init(showsTitle:)

Creates a unified window toolbar style.

macOS 11.0+

    
    
    init(showsTitle: Bool)

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.



# UIViewControllerRepresentableContext

Instance Property

# coordinator

The view’s associated coordinator.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    let coordinator: Representable.Coordinator

## See Also

### Coordinating view controller interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating view controller interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

Instance Property

# environment

Environment values that describe the current state of the system.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your UIKit view
controller when creating or updating it.



# UIHostingController

Initializer

# init(rootView:)

Creates a hosting controller object that wraps the specified SwiftUI view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    init(rootView: Content)

##  Parameters

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using the
hosting view controller.

## Return Value

A `UIHostingController` object initialized with the specified SwiftUI view.

## See Also

### Creating a hosting controller object

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

Initializer

# init(coder:rootView:)

Creates a hosting controller object from an archive and the specified SwiftUI
view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    init?(
        coder aDecoder: NSCoder,
        rootView: Content
    )

##  Parameters

`coder`

    

The decoder to use during initialization.

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using this
view controller.

## Return Value

A `UIViewController` object that you can present from your interface.

## See Also

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

Initializer

# init(coder:)

Creates a hosting controller object from the contents of the specified
archive.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    required dynamic init?(coder aDecoder: NSCoder)

## Discussion

The default implementation of this method throws an exception. To create your
view controller from an archive, override this method and initialize the
superclass using the `init(coder:rootView:)` method instead.

-Parameter coder: The decoder to use during initialization.

## See Also

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

Instance Method

# loadView()

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func loadView()

## See Also

### Responding to view-related events

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewWillAppear(_:)

Notifies the view controller that its view is about to be added to a view
hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewWillAppear(_ animated: Bool)

##  Parameters

`animated`

    

If `true`, the view is being added using an animation.

## Discussion

SwiftUI calls this method before adding the hosting controller’s root view to
the view hierarchy. You can override this method to perform custom tasks
associated with the appearance of the view. If you override this method, you
must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

`func loadView()`

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewDidAppear(_:)

Notifies the view controller that its view has been added to a view hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewDidAppear(_ animated: Bool)

##  Parameters

`animated`

    

If `true`, the view is being added using an animation.

## Discussion

SwiftUI calls this method after adding the hosting controller’s root view to
the view hierarchy. You can override this method to perform custom tasks
associated with the appearance of the view. If you override this method, you
must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewWillDisappear(_:)

Notifies the view controller that its view will be removed from a view
hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewWillDisappear(_ animated: Bool)

##  Parameters

`animated`

    

If `true`, the view is being removed using an animation.

## Discussion

SwiftUI calls this method before removing the hosting controller’s root view
from the view hierarchy. You can override this method to perform custom tasks
associated with the disappearance of the view. If you override this method,
you must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewDidDisappear(_:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewDidDisappear(_ animated: Bool)

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# willMove(toParent:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func willMove(toParent parent: UIViewController?)

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# didMove(toParent:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func didMove(toParent parent: UIViewController?)

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewWillTransition(to:with:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewWillTransition(
        to size: CGSize,
        with coordinator: any UIViewControllerTransitionCoordinator
    )

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# viewWillLayoutSubviews()

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func viewWillLayoutSubviews()

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# target(forAction:withSender:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func target(
        forAction action: Selector,
        withSender sender: Any?
    ) -> Any?

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    var rootView: Content { get set }

## See Also

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

Instance Property

# isModalInPresentation

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var isModalInPresentation: Bool { get set }

Instance Property

# sizingOptions

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    @MainActor
    var sizingOptions: UIHostingControllerSizingOptions { get set }

## Discussion

The default value is the empty set.

## See Also

### Managing the size

`func preferredContentSizeDidChange(forChildContentContainer: any
UIContentContainer)`

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Available when `Content` conforms to `View`.

Instance Method

# preferredContentSizeDidChange(forChildContentContainer:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func preferredContentSizeDidChange(forChildContentContainer container: any UIContentContainer)

## See Also

### Managing the size

`var sizingOptions: UIHostingControllerSizingOptions`

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Available when `Content` conforms to `View`.

Instance Method

# sizeThatFits(in:)

Calculates and returns the most appropriate size for the current view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    func sizeThatFits(in size: CGSize) -> CGSize

##  Parameters

`size`

    

The proposed new size for the view.

## Return Value

The size that offers the best fit for the root view and its contents.

## See Also

### Managing the size

`var sizingOptions: UIHostingControllerSizingOptions`

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

`func preferredContentSizeDidChange(forChildContentContainer: any
UIContentContainer)`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Available when `Content` conforms to `View`.

Instance Property

# safeAreaRegions

The safe area regions that this view controller adds to its view.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    var safeAreaRegions: SafeAreaRegions { get set }

Available when `Content` conforms to `View`.

## Discussion

An example of when this is appropriate to use is when hosting content that you
know should never be affected by the safe area, such as a custom scrollable
container. Disabling a safe area region omits it from the SwiftUI layout
system altogether.

The default value is `SafeAreaRegions.all`.

## See Also

### Managing the size

`var sizingOptions: UIHostingControllerSizingOptions`

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

`func preferredContentSizeDidChange(forChildContentContainer: any
UIContentContainer)`

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

Instance Property

# preferredStatusBarStyle

The preferred status bar style for the view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var preferredStatusBarStyle: UIStatusBarStyle { get }

## See Also

### Configuring the status bar

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarStyle: UIViewController?`

`var childForStatusBarHidden: UIViewController?`

Instance Property

# preferredStatusBarUpdateAnimation

The animation style to use when hiding or showing the status bar for this view
controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var preferredStatusBarUpdateAnimation: UIStatusBarAnimation { get }

## See Also

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarStyle: UIViewController?`

`var childForStatusBarHidden: UIViewController?`

Instance Property

# prefersStatusBarHidden

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var prefersStatusBarHidden: Bool { get }

## See Also

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var childForStatusBarStyle: UIViewController?`

`var childForStatusBarHidden: UIViewController?`

Instance Property

# childForStatusBarStyle

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var childForStatusBarStyle: UIViewController? { get }

## See Also

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarHidden: UIViewController?`

Instance Property

# childForStatusBarHidden

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var childForStatusBarHidden: UIViewController? { get }

## See Also

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarStyle: UIViewController?`

Instance Property

# prefersHomeIndicatorAutoHidden

A Boolean value that indicates whether the view controller prefers the home
indicator to be hidden or shown.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var prefersHomeIndicatorAutoHidden: Bool { get }

## See Also

### Configuring the home indicator

`var childForHomeIndicatorAutoHidden: UIViewController?`

Instance Property

# childForHomeIndicatorAutoHidden

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var childForHomeIndicatorAutoHidden: UIViewController? { get }

## See Also

### Configuring the home indicator

`var prefersHomeIndicatorAutoHidden: Bool`

A Boolean value that indicates whether the view controller prefers the home
indicator to be hidden or shown.

Instance Property

# preferredUserInterfaceStyle

The preferred interface style for this view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var preferredUserInterfaceStyle: UIUserInterfaceStyle { get }

## See Also

### Configuring the interface appearance

`var preferredScreenEdgesDeferringSystemGestures: UIRectEdge`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`var childForScreenEdgesDeferringSystemGestures: UIViewController?`

Instance Property

# preferredScreenEdgesDeferringSystemGestures

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var preferredScreenEdgesDeferringSystemGestures: UIRectEdge { get }

## See Also

### Configuring the interface appearance

`var preferredUserInterfaceStyle: UIUserInterfaceStyle`

The preferred interface style for this view controller.

`var childForScreenEdgesDeferringSystemGestures: UIViewController?`

Instance Property

# childForScreenEdgesDeferringSystemGestures

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var childForScreenEdgesDeferringSystemGestures: UIViewController? { get }

## See Also

### Configuring the interface appearance

`var preferredUserInterfaceStyle: UIUserInterfaceStyle`

The preferred interface style for this view controller.

`var preferredScreenEdgesDeferringSystemGestures: UIRectEdge`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

Instance Property

# keyCommands

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var keyCommands: [UIKeyCommand]? { get }

Instance Property

# undoManager

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var undoManager: UndoManager? { get }

Instance Property

# childViewControllerForPreferredContainerBackgroundStyle

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var childViewControllerForPreferredContainerBackgroundStyle: UIViewController? { get }

Instance Property

# preferredContainerBackgroundStyle

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic var preferredContainerBackgroundStyle: UIContainerBackgroundStyle { get }

Instance Method

# addChild(_:)

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    override dynamic func addChild(_ childController: UIViewController)



# UIKit integration

Class

# UIHostingController

A UIKit view controller that manages a SwiftUI view hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    @MainActor
    class UIHostingController<Content> where Content : View

## Overview

Create a `UIHostingController` object when you want to integrate SwiftUI views
into a UIKit view hierarchy. At creation time, specify the SwiftUI view you
want to use as the root view for this view controller; you can change that
view later using the `rootView` property. Use the hosting controller like you
would any other view controller, by presenting it or embedding it as a child
view controller in your interface.

## Topics

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

`init?(coder: NSCoder)`

Creates a hosting controller object from the contents of the specified
archive.

### Responding to view-related events

`func loadView()`

`func viewWillAppear(Bool)`

Notifies the view controller that its view is about to be added to a view
hierarchy.

`func viewDidAppear(Bool)`

Notifies the view controller that its view has been added to a view hierarchy.

`func viewWillDisappear(Bool)`

Notifies the view controller that its view will be removed from a view
hierarchy.

`func viewDidDisappear(Bool)`

`func willMove(toParent: UIViewController?)`

`func didMove(toParent: UIViewController?)`

`func viewWillTransition(to: CGSize, with: any
UIViewControllerTransitionCoordinator)`

`func viewWillLayoutSubviews()`

`func target(forAction: Selector, withSender: Any?) -> Any?`

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

### Checking for modality

`var isModalInPresentation: Bool`

### Managing the size

`var sizingOptions: UIHostingControllerSizingOptions`

The options for how the hosting controller tracks changes to the size of its
SwiftUI content.

`func preferredContentSizeDidChange(forChildContentContainer: any
UIContentContainer)`

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Available when `Content` conforms to `View`.

### Configuring the status bar

`var preferredStatusBarStyle: UIStatusBarStyle`

The preferred status bar style for the view controller.

`var preferredStatusBarUpdateAnimation: UIStatusBarAnimation`

The animation style to use when hiding or showing the status bar for this view
controller.

`var prefersStatusBarHidden: Bool`

A Boolean value that indicates whether the view controller prefers the status
bar to be hidden or shown.

`var childForStatusBarStyle: UIViewController?`

`var childForStatusBarHidden: UIViewController?`

### Configuring the home indicator

`var prefersHomeIndicatorAutoHidden: Bool`

A Boolean value that indicates whether the view controller prefers the home
indicator to be hidden or shown.

`var childForHomeIndicatorAutoHidden: UIViewController?`

### Configuring the interface appearance

`var preferredUserInterfaceStyle: UIUserInterfaceStyle`

The preferred interface style for this view controller.

`var preferredScreenEdgesDeferringSystemGestures: UIRectEdge`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`var childForScreenEdgesDeferringSystemGestures: UIViewController?`

### Accessing the available key commands

`var keyCommands: [UIKeyCommand]?`

### Managing undo

`var undoManager: UndoManager?`

### Instance Properties

`var childViewControllerForPreferredContainerBackgroundStyle:
UIViewController?`

`var preferredContainerBackgroundStyle: UIContainerBackgroundStyle`

### Instance Methods

`func addChild(UIViewController)`

## Relationships

### Inherits From

  * `UIViewController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSCoding`
  * `NSExtensionRequestHandling`
  * `NSObjectProtocol`
  * `NSTouchBarProvider`
  * `UIActivityItemsConfigurationProviding`
  * `UIAppearanceContainer`
  * `UIContentContainer`
  * `UIFocusEnvironment`
  * `UIPasteConfigurationSupporting`
  * `UIResponderStandardEditActions`
  * `UIStateRestoring`
  * `UITraitChangeObservable`
  * `UITraitEnvironment`
  * `UIUserActivityRestoring`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`struct UIHostingControllerSizingOptions`

Options for how a hosting controller tracks its content’s size.

`struct UIHostingConfiguration`

A content configuration suitable for hosting a hierarchy of SwiftUI views.

Structure

# UIHostingControllerSizingOptions

Options for how a hosting controller tracks its content’s size.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct UIHostingControllerSizingOptions

## Topics

### Getting sizing options

`static let intrinsicContentSize: UIHostingControllerSizingOptions`

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

`static let preferredContentSize: UIHostingControllerSizingOptions`

The hosting controller tracks its content’s ideal size in its preferred
content size.

### Creating a sizing option

`init(rawValue: Int)`

Creates a new option set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`class UIHostingController`

A UIKit view controller that manages a SwiftUI view hierarchy.

`struct UIHostingConfiguration`

A content configuration suitable for hosting a hierarchy of SwiftUI views.

Structure

# UIHostingConfiguration

A content configuration suitable for hosting a hierarchy of SwiftUI views.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS 1.0+

    
    
    struct UIHostingConfiguration<Content, Background> where Content : View, Background : View

## Overview

Use a value of this type, which conforms to the `UIContentConfiguration`
protocol, with a `UICollectionViewCell` or `UITableViewCell` to host a
hierarchy of SwiftUI views in a collection or table view, respectively. For
example, the following shows a stack with an image and text inside the cell:

You can also customize the background of the containing cell. The following
example draws a blue background:

When used in a list layout, certain APIs are bridged automatically, like swipe
actions and separator alignment. The following example shows a trailing yellow
star swipe action:

## Topics

### Creating and updating a configuration

`init(content: () -> Content)`

Creates a hosting configuration with the given contents.

Available when `Content` conforms to `View` and `Background` is `EmptyView`.

### Setting the background

`func background<S>(S) -> UIHostingConfiguration<Content,
_UIHostingConfigurationBackgroundView<S>>`

Sets the background contents for the hosting configuration’s enclosing cell.

`func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>`

Sets the background contents for the hosting configuration’s enclosing cell.

### Setting margins

`func margins(Edge.Set, EdgeInsets) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

`func margins(Edge.Set, CGFloat) -> UIHostingConfiguration<Content,
Background>`

Sets the margins around the content of the configuration.

### Setting a size

`func minSize(width: CGFloat?, height: CGFloat?) ->
UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

`func minSize() -> UIHostingConfiguration<Content, Background>`

Sets the minimum size for the configuration.

Deprecated

## Relationships

### Conforms To

  * `UIContentConfiguration`

## See Also

### Displaying SwiftUI views in UIKit

Using SwiftUI with UIKit

Learn how to incorporate SwiftUI views into a UIKit app.

`class UIHostingController`

A UIKit view controller that manages a SwiftUI view hierarchy.

`struct UIHostingControllerSizingOptions`

Options for how a hosting controller tracks its content’s size.

Protocol

# UIViewRepresentable

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    protocol UIViewRepresentable : View where Self.Body == Never

## Overview

Use a `UIViewRepresentable` instance to create and manage a `UIView` object in
your SwiftUI interface. Adopt this protocol in one of your app’s custom
instances, and use its methods to create, update, and tear down your view. The
creation and update processes parallel the behavior of SwiftUI views, and you
use them to configure your view with your app’s current state information. Use
the teardown process to remove your view cleanly from your SwiftUI. For
example, you might use the teardown process to notify other objects that the
view is disappearing.

To add your view into your SwiftUI interface, create your
`UIViewRepresentable` instance and add it to your SwiftUI interface. The
system calls the methods of your representable instance at appropriate times
to create and update the view. The following example shows the inclusion of a
custom `MyRepresentedCustomView` structure in the view hierarchy.

The system doesn’t automatically communicate changes occurring within your
view to other parts of your SwiftUI interface. When you want your view to
coordinate with other SwiftUI views, you must provide a `Coordinator` instance
to facilitate those interactions. For example, you use a coordinator to
forward target-action and delegate messages from your view to any SwiftUI
views.

## Topics

### Creating and updating the view

`func makeUIView(context: Self.Context) -> Self.UIViewType`

Creates the view object and configures its initial state.

**Required**

` func updateUIView(Self.UIViewType, context: Self.Context)`

Updates the state of the specified view with new information from SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewType : UIView`

The type of view to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, uiView: Self.UIViewType, context:
Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view

`static func dismantleUIView(Self.UIViewType, coordinator: Self.Coordinator)`

Cleans up the presented UIKit view (and coordinator) in anticipation of their
removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the view.

**Required**

### Performing layout

`typealias LayoutOptions`

## Relationships

### Inherits From

  * `View`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Structure

# UIViewRepresentableContext

Contextual information about the state of the system that you use to create
and update your UIKit view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    struct UIViewRepresentableContext<Representable> where Representable : UIViewRepresentable

## Overview

A `UIViewRepresentableContext` structure contains details about the current
state of the system. When creating and updating your view, the system creates
one of these structures and passes it to the appropriate method of your custom
`UIViewRepresentable` instance. Use the information in this structure to
configure your view. For example, use the provided environment values to
configure the appearance of your view. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

`var transaction: Transaction`

The current transaction.

### Getting the current environment data

`var environment: EnvironmentValues`

The current environment.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Protocol

# UIViewControllerRepresentable

A view that represents a UIKit view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    protocol UIViewControllerRepresentable : View where Self.Body == Never

## Overview

Use a `UIViewControllerRepresentable` instance to create and manage a
`UIViewController` object in your SwiftUI interface. Adopt this protocol in
one of your app’s custom instances, and use its methods to create, update, and
tear down your view controller. The creation and update processes parallel the
behavior of SwiftUI views, and you use them to configure your view controller
with your app’s current state information. Use the teardown process to remove
your view controller cleanly from your SwiftUI. For example, you might use the
teardown process to notify other objects that the view controller is
disappearing.

To add your view controller into your SwiftUI interface, create your
`UIViewControllerRepresentable` instance and add it to your SwiftUI interface.
The system calls the methods of your custom instance at appropriate times.

The system doesn’t automatically communicate changes occurring within your
view controller to other parts of your SwiftUI interface. When you want your
view controller to coordinate with other SwiftUI views, you must provide a
`Coordinator` instance to facilitate those interactions. For example, you use
a coordinator to forward target-action and delegate messages from your view
controller to any SwiftUI views.

## Topics

### Creating and updating the view controller

`func makeUIViewController(context: Self.Context) ->
Self.UIViewControllerType`

Creates the view controller object and configures its initial state.

**Required**

` func updateUIViewController(Self.UIViewControllerType, context:
Self.Context)`

Updates the state of the specified view controller with new information from
SwiftUI.

**Required**

` typealias Context`

`associatedtype UIViewControllerType : UIViewController`

The type of view controller to present.

**Required**

### Specifying a size

`func sizeThatFits(ProposedViewSize, uiViewController:
Self.UIViewControllerType, context: Self.Context) -> CGSize?`

Given a proposed size, returns the preferred size of the composite view.

**Required** Default implementation provided.

### Cleaning up the view controller

`static func dismantleUIViewController(Self.UIViewControllerType, coordinator:
Self.Coordinator)`

Cleans up the presented view controller (and coordinator) in anticipation of
their removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your view
controller to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the view controller.

**Required**

### Performing layout

`typealias LayoutOptions`

## Relationships

### Inherits From

  * `View`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`struct UIViewControllerRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

Structure

# UIViewControllerRepresentableContext

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    @MainActor
    struct UIViewControllerRepresentableContext<Representable> where Representable : UIViewControllerRepresentable

## Overview

A `UIViewControllerRepresentableContext` structure contains details about the
current state of the system. When creating and updating your view controller,
the system creates one of these structures and passes it to the appropriate
method of your custom `UIViewControllerRepresentable` instance. Use the
information in this structure to configure your view controller. For example,
use the provided environment values to configure the appearance of your view
controller and views. Don’t create this structure yourself.

## Topics

### Coordinating view controller interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

`var transaction: Transaction`

The current transaction.

### Getting the environment data

`var environment: EnvironmentValues`

Environment values that describe the current state of the system.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adding UIKit views to SwiftUI view hierarchies

`protocol UIViewRepresentable`

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

`struct UIViewRepresentableContext`

Contextual information about the state of the system that you use to create
and update your UIKit view.

`protocol UIViewControllerRepresentable`

A view that represents a UIKit view controller.

Protocol

# UITraitBridgedEnvironmentKey

An environment key that is bridged to a UIKit trait.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    protocol UITraitBridgedEnvironmentKey : EnvironmentKey

## Overview

Use this protocol to allow the same underlying data to be accessed using an
environment key in SwiftUI and trait in UIKit. As the bridging is
bidirectional, values written to the trait in UIKit can be read using the
environment key in SwiftUI, and values written to the environment key in
SwiftUI can be read from the trait in UIKit.

Given a custom UIKit trait named `MyTrait` with `myTrait` properties on both
`UITraitCollection` and `UIMutableTraits`:

You can declare an environment key to represent the same data:

Bridge the environment key and the trait by conforming to the
`UITraitBridgedEnvironmentKey` protocol, providing implementations of
`read(from:)` and `write(to:value:)` to losslessly convert the environment
value from and to the corresponding trait value:

## Topics

### Managing the keys

`static func read(from: UITraitCollection) -> Self.Value`

Reads the trait value from the trait collection, and returns the equivalent
environment value.

**Required**

` static func write(to: inout any UIMutableTraits, value: Self.Value)`

**Required**

## Relationships

### Inherits From

  * `EnvironmentKey`

Class

# UIHostingOrnament

A model that represents an ornament suitable for being hosted in UIKit.

visionOS 1.0+

    
    
    class UIHostingOrnament<Content> where Content : View

## Overview

Use a `UIHostingOrnament` when you want to add ornaments to a UIKit view
controller. For example, the following adds a single bottom ornament to the
current view controller:

## Topics

### Creating a hosting ornament

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this ornament.

### Setting the alignment

`var contentAlignment: Alignment`

The alignment in the ornament used to position it.

### Initializers

`init(sceneAnchor: UnitPoint, contentAlignment: Alignment, content: () ->
Content)`

Creates an ornament with the specified alignment and content.

### Instance Properties

`var sceneAnchor: UnitPoint`

The anchor point for aligning the ornament’s content (based on the
`contentAlignment`) with the scene.

## Relationships

### Inherits From

  * `UIOrnament`

## See Also

### Hosting an ornament in UIKit

`class UIOrnament`

The abstract base class that represents an ornament.

Class

# UIOrnament

The abstract base class that represents an ornament.

visionOS 1.0+

    
    
    class UIOrnament

## Overview

You don’t create an instance of this class directly. Instead use
`UIHostingOrnament` when you want to add ornaments to a UIKit view controller.

## Relationships

### Inherited By

  * `UIHostingOrnament`

## See Also

### Hosting an ornament in UIKit

`class UIHostingOrnament`

A model that represents an ornament suitable for being hosted in UIKit.



