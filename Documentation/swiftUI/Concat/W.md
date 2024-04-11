# WindowBackgroundShapeStyle

Initializer

# init()

Creates a new window background shape style instance.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init()



# WheelPickerStyle

Initializer

# init()

Sets the picker style to display an item wheel from which the user makes a
selection.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 6.0+  visionOS 1.0+

    
    
    init()



# WheelDatePickerStyle

Initializer

# init()

Creates an instance of the wheel date picker style.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    init()



# WindowToolbarStyle

Type Property

# automatic

The automatic window toolbar style.

macOS 11.0+

    
    
    static var automatic: DefaultWindowToolbarStyle { get }

Available when `Self` is `DefaultWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# expanded

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    static var expanded: ExpandedWindowToolbarStyle { get }

Available when `Self` is `ExpandedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unified

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static var unified: UnifiedWindowToolbarStyle { get }

Available when `Self` is `UnifiedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unified(showsTitle:)

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle

Available when `Self` is `UnifiedWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unifiedCompact

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static var unifiedCompact: UnifiedCompactWindowToolbarStyle { get }

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unifiedCompact(showsTitle:)

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Structure

# DefaultWindowToolbarStyle

The default window toolbar style.

macOS 11.0+

    
    
    struct DefaultWindowToolbarStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a default window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# ExpandedWindowToolbarStyle

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    struct ExpandedWindowToolbarStyle

## Overview

You can also use `expanded` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates an expanded window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedWindowToolbarStyle

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    struct UnifiedWindowToolbarStyle

## Overview

You can also use `unified` or `unified(showsTitle:)` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedCompactWindowToolbarStyle

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    struct UnifiedCompactWindowToolbarStyle

## Overview

You can also use `unifiedCompact` or `unifiedCompact(showsTitle:)` to
construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Type Property

# automatic

The automatic window toolbar style.

macOS 11.0+

    
    
    static var automatic: DefaultWindowToolbarStyle { get }

Available when `Self` is `DefaultWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# expanded

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    static var expanded: ExpandedWindowToolbarStyle { get }

Available when `Self` is `ExpandedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unified

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static var unified: UnifiedWindowToolbarStyle { get }

Available when `Self` is `UnifiedWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unified(showsTitle:)

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle

Available when `Self` is `UnifiedWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Property

# unifiedCompact

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static var unifiedCompact: UnifiedCompactWindowToolbarStyle { get }

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Type Method

# unifiedCompact(showsTitle:)

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    static func unifiedCompact(showsTitle: Bool) -> UnifiedCompactWindowToolbarStyle

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

##  Parameters

`showsTitle`

    

Whether the title should be displayed.

## See Also

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

Structure

# DefaultWindowToolbarStyle

The default window toolbar style.

macOS 11.0+

    
    
    struct DefaultWindowToolbarStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a default window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# ExpandedWindowToolbarStyle

A window toolbar style which displays its title bar area above the toolbar.

macOS 11.0+

    
    
    struct ExpandedWindowToolbarStyle

## Overview

You can also use `expanded` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates an expanded window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedWindowToolbarStyle

A window toolbar style which displays its toolbar and title bar inline.

macOS 11.0+

    
    
    struct UnifiedWindowToolbarStyle

## Overview

You can also use `unified` or `unified(showsTitle:)` to construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified window toolbar style.

`init(showsTitle: Bool)`

Creates a unified window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Structure

# UnifiedCompactWindowToolbarStyle

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

macOS 11.0+

    
    
    struct UnifiedCompactWindowToolbarStyle

## Overview

You can also use `unifiedCompact` or `unifiedCompact(showsTitle:)` to
construct this style.

## Topics

### Creating the window toolbar style

`init()`

Creates a unified compact window toolbar style.

`init(showsTitle: Bool)`

Creates a unified compact window toolbar style.

## Relationships

### Conforms To

  * `WindowToolbarStyle`

## See Also

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.



# WKHostingController

Initializer

# init()

Creates a hosting controller object that you can use to implement your app’s
main interface using SwiftUI views

watchOS 6.0+

    
    
    @MainActor
    override dynamic init()

Instance Property

# body

The root view of the view hierarchy to display for your interface controller.

watchOS 6.0+

    
    
    @MainActor
    var body: Body { get }

## Discussion

Override this property and return the root view of your SwiftUI view hierarchy
from your implementation. If you don’t override this property, accessing the
default implementation triggers an exception.

Instance Method

# updateBodyIfNeeded()

Updates the interface controller’s set of views immediately, if updates are
pending.

watchOS 6.0+

    
    
    @MainActor
    func updateBodyIfNeeded()

## Discussion

Calling this method forces the hosting controller to update its current set of
views, but only if there are pending changes. If there are no pending changes,
this method does nothing.

To mark the interface controller as needing an update, call
`setNeedsBodyUpdate()`.

## See Also

### Updating the root view

`func setNeedsBodyUpdate()`

Invalidates the current SwiftUI views and triggers an update during the next
cycle.

Instance Method

# setNeedsBodyUpdate()

Invalidates the current SwiftUI views and triggers an update during the next
cycle.

watchOS 6.0+

    
    
    @MainActor
    func setNeedsBodyUpdate()

## Discussion

Call this method to mark the views of the hosting controller as needing an
update. During the next update cycle, the hosting controller fetches an
updated set of views from its `body` property.

## See Also

### Updating the root view

`func updateBodyIfNeeded()`

Updates the interface controller’s set of views immediately, if updates are
pending.



# WKInterfaceObjectRepresentableContext

Instance Property

# coordinator

The view’s associated coordinator.

watchOS 6.0+

    
    
    @MainActor
    let coordinator: Representable.Coordinator

## See Also

### Coordinating interactions

`var transaction: Transaction`

The current transaction.

Instance Property

# transaction

The current transaction.

watchOS 6.0+

    
    
    @MainActor
    var transaction: Transaction { get }

## See Also

### Coordinating interactions

`let coordinator: Representable.Coordinator`

The view’s associated coordinator.

Instance Property

# environment

The current environment.

watchOS 6.0+

    
    
    @MainActor
    var environment: EnvironmentValues { get }

## Discussion

Use the environment values to configure the state of your interface object
when creating or updating it.



# WindowResizability

Type Property

# automatic

The automatic window resizability.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: WindowResizability { get set }

## Discussion

When you use automatic resizability, SwiftUI applies a resizing strategy
that’s appropriate for the scene type:

  * Windows from `WindowGroup`, `Window`, and `DocumentGroup` scene declarations use the `contentMinSize` strategy.

  * A window from a `Settings` scene declaration uses the `contentSize` strategy.

Automatic resizability is the default if you don’t specify another value using
the `windowResizability(_:)` scene modifier.

## See Also

### Getting the resizability

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

Type Property

# contentMinSize

A window resizability that’s partially derived from the window’s content.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var contentMinSize: WindowResizability { get set }

## Discussion

Windows that use this resizability have:

  * A minimum size that matches the minimum size of the window’s content.

  * No maximum size.

## See Also

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

Type Property

# contentSize

A window resizability that’s derived from the window’s content.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var contentSize: WindowResizability { get set }

## Discussion

Windows that use this resizability have:

  * A minimum size that matches the minimum size of the window’s content.

  * A maximum size that matches the maximum size of the window’s content.

## See Also

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.



# WKApplicationDelegateAdaptor

Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

Note

the instantiated delegate will be placed in the Environment and may be
accessed by using the `@EnvironmentObject` property wrapper in the view
hierarchy.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 10.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

Note

the instantiated delegate will be placed in the Environment and may be
accessed by using the `@Environment` property wrapper in the view hierarchy.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

Instance Property

# projectedValue

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

watchOS 7.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get
the `projectedValue`, prefix the property variable with `$`.

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying delegate.

Instance Property

# wrappedValue

The underlying delegate.

watchOS 7.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.



# Windows

Structure

# WindowGroup

A scene that presents a group of identically structured windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct WindowGroup<Content> where Content : View

## Overview

Use a `WindowGroup` as a container for a view hierarchy that your app
presents. The hierarchy that you declare as the group’s content serves as a
template for each window that the app creates from that group:

SwiftUI takes care of certain platform-specific behaviors. For example, on
platforms that support it, like macOS and iPadOS, people can open more than
one window from the group simultaneously. In macOS, people can gather open
windows together in a tabbed interface. Also in macOS, window groups
automatically provide commands for standard window management.

Important

To enable an iPadOS app to simultaneously display multiple windows, be sure to
include the `UIApplicationSupportsMultipleScenes` key with a value of `true`
in the UIApplicationSceneManifest dictionary of your app’s Information
Property List.

Every window in the group maintains independent state. For example, the system
allocates new storage for any `State` or `StateObject` variables instantiated
by the scene’s view hierarchy for each window that it creates.

For document-based apps, use `DocumentGroup` to define windows instead.

### Open windows programmatically

If you initialize a window group with an identifier, a presentation type, or
both, you can programmatically open a window from the group. For example, you
can give the mail viewer scene from the previous example an identifier:

Elsewhere in your code, you can use the `openWindow` action from the
environment to create a new window from the group:

Be sure to use unique strings for identifiers that you apply to window groups
in your app.

### Present data in a window

If you initialize a window group with a presentation type, you can pass data
of that type to the window when you open it. For example, you can define a
second window group for the Mail app that displays a specified message:

When you call the `openWindow` action with a value, SwiftUI finds the window
group with the matching type and passes a binding to the value into the window
group’s content closure. For example, you can define a button that opens a
message by passing the message’s identifier:

Be sure that the type you present conforms to both the `Hashable` and
`Codable` protocols. Also, prefer lightweight data for the presentation value.
For model values that conform to the `Identifiable` protocol, the value’s
identifier works well as a presentation type, as the above example
demonstrates.

If a window with a binding to the same value that you pass to the `openWindow`
action already appears in the user interface, the system brings the existing
window to the front rather than opening a new window. If SwiftUI doesn’t have
a value to provide — for example, when someone opens a window by choosing File
> New Window from the macOS menu bar — SwiftUI passes a binding to a `nil`
value instead. To avoid receiving a `nil` value, you can optionally specify a
default value in your window group initializer. For example, for the message
viewer, you can present a new empty message:

SwiftUI persists the value of the binding for the purposes of state
restoration, and reapplies the same value when restoring the window. If the
restoration process results in an error, SwiftUI sets the binding to the
default value if you provide one, or `nil` otherwise.

### Title your app’s windows

To help people distinguish among windows from different groups, include a
title as the first parameter in the group’s initializer:

SwiftUI uses this title when referring to the window in:

  * The list of new windows that someone can open using the File > New menu.

  * The window’s title bar.

  * The list of open windows that the Window menu displays.

If you don’t provide a title for a window, the system refers to the window
using the app’s name instead.

Note

You can override the title that SwiftUI uses for a window in the window’s
title bar and the menu’s list of open windows by adding one of the
`navigationTitle(_:)` modifiers to the window’s content. This enables you to
customize and dynamically update the title for each individual window
instance.

### Distinguish windows that present like data

To programmatically distinguish between windows that present the same type of
data, like when you use a `UUID` as the identifier for more than one model
type, add the `id` parameter to the group’s initializer to provide a unique
string identifier:

Then use both the identifer and a value to open the window:

### Dismiss a window programmatically

The system provides people with platform-appropriate controls to dismiss a
window. You can also dismiss windows programmatically by calling the `dismiss`
action from within the window’s view hierarchy. For example, you can include a
button in the account detail view from the previous example that dismisses the
view:

The dismiss action doesn’t close the window if you call it from a modal — like
a sheet or a popover — that you present from the window. In that case, the
action dismisses the modal presentation instead.

## Topics

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

### Supporting types

`struct PresentedWindowContent`

A view that represents the content of a presented window.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct Window`

A scene that presents its content in a single, unique window.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

Structure

# Window

A scene that presents its content in a single, unique window.

macOS 13.0+

    
    
    struct Window<Content> where Content : View

## Overview

Use a `Window` scene to augment the main interface of your app with a window
that gives people access to supplemental functionality. For example, you can
create a secondary window in a mail reader app that enables people to view the
status of their account connections:

Provide a title as the first argument to the window’s intializer. The system
uses the title to identify the window to people using your app in the window’s
title bar or in the list of available singleton windows that the Windows menu
displays automatically.

Note

You can override the title in the window’s title bar by adding one of the
`navigationTitle(_:)` view modifiers to the window’s content. This enables you
to dynamically update the title bar.

### Open a window programmatically

People open the window by selecting it in the Windows menu, but you can also
open the window programmatically using the `openWindow` action that you read
from the environment. Use the `id` parameter that you initialize the window
with to indicate which window to open. For example, you can create a button to
open the window from the previous example:

If the window is already open when you call this action, the action brings the
open window to the front. Be sure to use unique identifiers across all of the
`Window` and `WindowGroup` instances that you define.

### Dismiss a window programmatically

The system provides people with controls to close windows, but you can also
close a window programmatically using the `dismiss` action from within the
window’s view hierarchy. For example, you can include a button in the
connection doctor view that dismisses the view:

The dismiss action doesn’t close the window if you call it from a modal — like
a sheet or a popover — that you present from within the window. In that case,
the action dismisses the modal presentation instead.

### Use a window as the main scene

You can use a window as the main scene of your app when multi-window
functionality isn’t appropriate. For example, it might not make sense to
display more than one window for a video call app that relies on a hardware
resource, like a camera:

If your app uses a single window as its primary scene, the app quits when the
window closes. This behavior differs from an app that uses a `WindowGroup` as
its primary scene, where the app continues to run even after closing all of
its windows.

Note

In most cases it’s best to use a `WindowGroup` to represent the main scene of
your app. A window group provides multi-window functionality on platforms that
support it, like iPadOS and macOS, and makes it easier to share code across
platforms.

## Topics

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

Protocol

# WindowStyle

A specification for the appearance and interaction of a window.

macOS 11.0+  visionOS 1.0+

    
    
    protocol WindowStyle

## Topics

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

## Relationships

### Conforming Types

  * `DefaultWindowStyle`
  * `HiddenTitleBarWindowStyle`
  * `PlainWindowStyle`
  * `TitleBarWindowStyle`
  * `VolumetricWindowStyle`

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`struct Window`

A scene that presents its content in a single, unique window.

`func windowStyle<S>(S) -> some Scene`

Sets the style for windows created by this scene.

Instance Method

# windowStyle(_:)

Sets the style for windows created by this scene.

macOS 11.0+  visionOS 1.0+

    
    
    func windowStyle<S>(_ style: S) -> some Scene where S : WindowStyle
    

## See Also

### Creating windows

Bringing multiple windows to your SwiftUI app

Compose rich views by reacting to state changes and customize your app’s scene
presentation and behavior on iPadOS and macOS.

`struct WindowGroup`

A scene that presents a group of identically structured windows.

`struct Window`

A scene that presents its content in a single, unique window.

`protocol WindowStyle`

A specification for the appearance and interaction of a window.

Instance Method

# windowToolbarStyle(_:)

Sets the style for the toolbar defined within this scene.

macOS 11.0+

    
    
    func windowToolbarStyle<S>(_ style: S) -> some Scene where S : WindowToolbarStyle
    

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`protocol WindowToolbarStyle`

A specification for the appearance and behavior of a window’s toolbar.

Protocol

# WindowToolbarStyle

A specification for the appearance and behavior of a window’s toolbar.

macOS 11.0+

    
    
    protocol WindowToolbarStyle

## Topics

### Getting built-in window toolbar styles

`static var automatic: DefaultWindowToolbarStyle`

The automatic window toolbar style.

Available when `Self` is `DefaultWindowToolbarStyle`.

`static var expanded: ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

Available when `Self` is `ExpandedWindowToolbarStyle`.

`static var unified: UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`static func unified(showsTitle: Bool) -> UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

Available when `Self` is `UnifiedWindowToolbarStyle`.

`static var unifiedCompact: UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

`static func unifiedCompact(showsTitle: Bool) ->
UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

Available when `Self` is `UnifiedCompactWindowToolbarStyle`.

### Supporting types

`struct DefaultWindowToolbarStyle`

The default window toolbar style.

`struct ExpandedWindowToolbarStyle`

A window toolbar style which displays its title bar area above the toolbar.

`struct UnifiedWindowToolbarStyle`

A window toolbar style which displays its toolbar and title bar inline.

`struct UnifiedCompactWindowToolbarStyle`

A window toolbar style similar to `unified`, but with a more compact vertical
sizing.

## Relationships

### Conforming Types

  * `DefaultWindowToolbarStyle`
  * `ExpandedWindowToolbarStyle`
  * `UnifiedCompactWindowToolbarStyle`
  * `UnifiedWindowToolbarStyle`

## See Also

### Styling a toolbar

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func windowToolbarStyle<S>(S) -> some Scene`

Sets the style for the toolbar defined within this scene.

Article

# Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

## Overview

An app’s scenes, which contain views that people interact with, can take
different forms. For example, a scene can fill a window, a tab in a window, or
an entire screen. Some scenes can even place views throughout a person’s
surroundings. How a scene appears depends on its type, the platform, and the
context.

When someone launches your app, SwiftUI looks for the first `WindowGroup`,
`Window`, or `DocumentGroup` in your app declaration and opens a scene of that
type, typically filling a new window or the entire screen, depending on the
platform. For example, the following app running in macOS presents a window
that contains a `MailViewer` view:

In visionOS, you can alternatively configure your app to open the first
`ImmersiveSpace` that the app declares. In any case, specific platforms and
configurations enable you to open more than one scene at a time. Under those
conditions, you can use actions that appear in the environment to
programmatically open and close the scenes in your app.

### Check for multiple-scene support

If you share code among different platforms and need to find out at runtime
whether the current system supports displaying multiple scenes, read the
`supportsMultipleWindows` environment value. The following code creates a
button that’s hidden unless the app supports multiple windows:

The value that you read depends on both the platform and how you configure
your app:

  * In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.

  * In iPadOS and visionOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key `UIApplicationSupportsMultipleScenes` set to `true`, and `false` otherwise.

  * For all other platforms and configurations, the value returns `false`.

If your app only ever runs in one of these situations, you can assume the
associated behavior and don’t need to check the value.

### Enable multiple simultaneous scenes

You can always present multiple scenes in macOS. To enable an iPadOS or
visionOS app to simultaneously display multiple scenes — including
`ImmersiveSpace` scenes in visionOS — add the
`UIApplicationSupportsMultipleScenes` key with a value of `true` in the
UIApplicationSceneManifest dictionary of your app’s Information Property List.
Use the Info tab in Xcode for your app’s target to add this key:

Apps on other platforms can display only one scene during their lifetime.

### Open windows programmatically

Some platforms provide built-in controls that enable people to open instances
of the window-style scenes that your app defines. For example, in macOS people
can choose File > New Window from the menu bar to open a new window. SwiftUI
also provides ways for you to open new windows programmatically.

To do this, get the `openWindow` action from the environment and call it with
an identifier, a value, or both to indicate what kind of window to open and
optionally what data to open it with. The following view opens a new instance
of the previously defined mail viewer window when someone clicks or taps the
button:

When the action runs on a system that supports multiple scenes, SwiftUI looks
for a window in the app declaration that has a matching identifier and creates
a new scene of that type.

Important

If `supportsMultipleWindows` is `false` and you try to open a new window,
SwiftUI ignores the action and logs a runtime error.

In addition to opening more instances of an app’s main window, as in the above
example, you can also open other window types that your app’s body declares.
For example, you can open an instance of the `Window` that displays
connectivity information:

### Open a space programmatically

In visionOS, you open an immersive space — a scene that you can use to present
unbounded content in a person’s surroundings — in much the same way that you
open a window, except that you use the `openImmersiveSpace` action. The action
runs asynchronously, so you use the `await` keyword when you call it, and
typically do so from inside a `Task`:

Because your app operates in a Full Space when you open an `ImmersiveSpace`
scene, you can only open one scene of this type at a time. If you try to open
a space when one is already open, the system logs a runtime error.

Your app can display any number of windows together with an immersive space.
However, when you open a space from your app, the system hides all windows
that belong to other apps. After you dismiss your space, the other apps’
windows reappear. Similarly, the system hides your app’s windows if another
app opens an immersive space.

### Designate a space as your app’s main interface

When visionOS launches an app, it opens the first window group, window, or
document scene that the app’s body declares, just like on other platforms.
This is true even if you first declare a space. However, if you want to open
your app into an immersive space directly, specify a space as the default
scene for your app by adding the
`UIApplicationPreferredDefaultSceneSessionRole` key to your app’s information
property list and setting its value to
`UISceneSessionRoleImmersiveSpaceApplication`. In that case, visionOS opens
the first space that it finds in your app declaration.

Important

Be careful not to overwhelm people when starting your app with an immersive
space. For design guidance, see Immersive experiences.

### Close windows programmatically

People can close windows using system controls, like the close button built
into the frame around a macOS window. You can also close windows
programmatically. Get the `dismissWindow` action from the environment, and
call it using the identifier of the window that you want to dismiss:

In iPadOS and visionOS, the system ignores the dismiss action if you use it to
close a window that’s your app’s only open scene.

### Close spaces programmatically

To close a space, call the `dismissImmersiveSpace` action. Like the
corresponding open space action, the close action operates asynchronously and
requires the `await` keyword:

You don’t need to specify an identifier for this action, because there can
only ever be one space open at a time. Like with windows, you can’t dismiss a
space that’s your app’s only open scene.

### Transition between a window and a space

Because you can’t programmatically close the last open window or immersive
space in a visionOS app, be sure to open a new scene before closing the old
one. Pay particular attention to the sequencing when moving between a window
and an immersive space, because the space’s open and dismiss actions run
asynchronously.

For example, consider a chess game that begins by displaying a start button in
a window. When someone taps the button, the app dismisses the window and opens
an immersive space that presents a chess board. The following button
demonstrates proper sequencing by opening the space and then closing the
window:

In the above code, it’s important to include the `dismissWindow` action inside
the task, so that it waits until the `openImmersiveSpace` action completes. If
you put the action outside the task — either before or after — it might
execute before the asynchronous open action completes, when the window is
still the only open scene. In that case, the system opens the space but
doesn’t close the window.

## See Also

### SwiftUI

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

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

Structure

# OpenWindowAction

An action that presents a window.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct OpenWindowAction

## Overview

Use the `openWindow` environment value to get the instance of this structure
for a given `Environment`. Then call the instance to open a window. You call
the instance directly because it defines a `callAsFunction(id:)` method that
Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

You indicate which scene to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter, as in the above example.

  * A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.

  * Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type, like a `UUID`.

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

## Topics

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

## See Also

### Opening windows

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

`var supportsMultipleWindows: Bool`

A Boolean value that indicates whether the current platform supports opening
multiple windows.

`var openWindow: OpenWindowAction`

A window presentation action stored in a view’s environment.

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

Structure

# DismissWindowAction

An action that dismisses a window associated to a particular scene.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DismissWindowAction

## Overview

Use the `dismissWindow` environment value to get the instance of this
structure for a given `Environment`. Then call the instance to dismiss a
window. You call the instance directly because it defines a
`callAsFunction(id:)` method that Swift calls when you call the instance.

For example, you can define a button that closes an auxiliary window:

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

## See Also

### Closing windows

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`struct DismissBehavior`

Programmatic window dismissal behaviors.

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

Structure

# DismissAction

An action that dismisses a presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct DismissAction

## Overview

Use the `dismiss` environment value to get the instance of this structure for
a given `Environment`. Then call the instance to perform the dismissal. You
call the instance directly because it defines a `callAsFunction()` method that
Swift calls when you call the instance.

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

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the view if it is currently presented.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Structure

# DismissBehavior

Programmatic window dismissal behaviors.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct DismissBehavior

## Overview

Use values of this type to control window dismissal during the current
transaction.

For example, to dismiss windows showing a modal presentation that would
otherwise prohibit dismissal, use the `destructive` behavior:

## Topics

### Getting behaviors

`static let destructive: DismissBehavior`

The destructive dismiss behavior.

`static let interactive: DismissBehavior`

The interactive dismiss behavior.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Closing windows

`var dismissWindow: DismissWindowAction`

A window dismissal action stored in a view’s environment.

`struct DismissWindowAction`

An action that dismisses a window associated to a particular scene.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

Article

# Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

## Overview

visionOS and macOS enable people to move and resize windows. In some cases,
your app can use scene modifiers to influence a window’s initial geometry on
these platforms, as well as to specify the strategy that the system employs to
place minimum and maximum size limitations on a window. This kind of
configuration affects both windows and volumes, which are windows with the
`volumetric` window style.

Your ability to configure window size and position is subject to the following
constraints:

  * The system might be unable to fulfill your request. For example, if you specify a default size that’s outside the range of the window’s resizability, the system clamps the affected dimension to keep it in range.

  * Although you can change the window’s content, you can’t directly manipulate window position or size after the window appears. This ensures that people have full control over their workspace.

  * During state restoration, the system restores windows to their previous position and size.

Note

Windows in iPadOS occupy the full screen, or share the screen with another
window in Slide Over or Split View. You can’t programmatically affect window
geometry on that platform.

### Specify initial window position

In macOS, the first time your app opens a window from a particular scene
declaration, the system places the window at the center of the screen by
default. For scene types that support multiple simultaneous windows, the
system offsets each additional window by a small amount to avoid fully
obscuring existing windows.

You can override the default placement of the first window in macOS by
applying the `defaultPosition(_:)` scene modifier to indicate where to place
the window relative to the screen bounds. For example, you can request that
the system place a new window in the bottom trailing corner of the screen:

The system aligns the point in the window that corresponds to the specified
`UnitPoint` with the point in the screen that corresponds to the same unit
point. You can use a built-in unit point, like `bottomTrailing` in the above
example, or define a custom one.

Important

You can’t use `defaultPosition(_:)` in visionOS. The system always places new
windows directly in front of people, where they happen to be looking at the
moment the window opens. This helps to make people aware of new windows.

### Specify initial window size

You can indicate a default initial size for a new window that the system
creates from a `Scene` declaration by applying one of the default size scene
modifiers, like `defaultSize(width:height:)`. For example, you can request
that new windows that a `WindowGroup` generates occupy 600 points in the
x-dimension and 400 points in the y-dimension:

The system might clamp the actual size of the window depending on both the
window’s content and resizability settings.

### Specify window resizability

Both macOS and visionOS provide interface controls that enable people to
resize windows, within certain limits. For example, people can use the control
that appears when they look at the corner of a visionOS window to resize a
window on that platform.

Play

You can specify how the system limits window resizability. The default
resizability for all scenes is `automatic`. With that strategy, `Settings`
windows use the `contentSize` strategy, where both the minimum and maximum
window size match the respective minimum and maximum sizes of the content that
the window contains. Other scene types use `contentMinSize` by default, which
retains the minimum size restriction, but doesn’t limit the maximium size.

You can specify one of these resizability strategies explicitly by adding the
`windowResizability(_:)` scene modifier to a scene. For example, people can
resize windows from the following window group to between 100 and 400 points
in both dimensions because the frame modifier imposes those bounds on the
content view:

You can take this even further and enforce a specific size for a window with
content that has a fixed size.

### Specify a volume size

When you create a volume, which is a window with the `volumetric` style, you
can specify the volume’s size using one of the three-dimensional default size
modifiers, like `defaultSize(width:height:depth:in:)`. The following code
creates a volume that’s one meter on a side:

The volume maintains this size for its entire lifetime. People can’t change
the size of a volume at runtime.

Although you can specify a volume’s size in points, it’s typically better to
use physical units, like the above code which specifies a size in meters. This
is because the system renders a volume with fixed scaling rather than dynamic
scaling, unlike a regular window, which means the volume appears more like a
physical object than a user interface. For information about the different
kinds of scaling, see Spatial layout.

## See Also

### SwiftUI

Hello World

Use windows, volumes, and immersive spaces to teach people about the Earth.

Presenting windows and spaces

Open and close the scenes that make up your app’s interface.

Instance Method

# defaultPosition(_:)

Sets a default position for a window.

macOS 13.0+

    
    
    func defaultPosition(_ position: UnitPoint) -> some Scene
    

##  Parameters

`position`

    

A `UnitPoint` that specifies where to place a newly opened window relative to
the screen bounds.

## Return Value

A scene that uses a default position for new windows.

## Discussion

The first time your app opens a window from a particular scene declaration,
the system places the window at the center of the screen by default. For scene
types that support multiple simultaneous windows, the system offsets each
additional window by a small amount to avoid completely obscuring existing
windows.

You can override the default placement of the first window by applying a scene
modifier that indicates where to place the window relative to the screen
bounds. For example, you can request that the system place a new window in the
bottom trailing corner of the screen:

The system aligns the point in the window that corresponds to the specified
`UnitPoint` with the point in the screen that corresponds to the same unit
point.

You typically use one of the predefined unit points — like `bottomTrailing` in
the above example — but you can also use a custom unit point. For example, the
following modifier aligns the point that’s one quarter of the way from the
leading edge of the window with the point that’s one quarter of the way from
the leading edge of the screen, while centering the window in the y-dimension:

The modifier affects any scene type that creates windows in macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

The value that you provide acts only as an initial default. During state
restoration, the system restores the window to the position that it last
occupied.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:)

Sets a default size for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func defaultSize(_ size: CGSize) -> some Scene
    

##  Parameters

`size`

    

The default size for new windows created from a scene.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this scene modifier to indicate a default initial size for a new window
that the system creates from a `Scene` declaration. For example, you can
request that new windows that a `WindowGroup` generates occupy 600 points in
the x-dimension and 400 points in the y-dimension:

The size that you specify acts only as a default for when the window first
appears. People can later resize the window using interface controls that the
system provides. Also, during state restoration, the system restores windows
to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s
inherent resizability in one or both dimensions, the system clamps the
affected dimension to keep it in range. You can configure the resizability of
a scene using the `windowResizability(_:)` modifier.

The default size modifier affects any scene type that creates windows in
macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

If you want to specify the input directly in terms of width and height, use
`defaultSize(width:height:)` instead.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(_ size: Size3D) -> some Scene
    

##  Parameters

`size`

    

The default 3D size for the created window.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

    
    
    WindowGroup {
        ContentView()
    }
    .windowStyle(.volumetric)
    .defaultSize(Size3D(width: 600, height: 400, depth: 600))
    

Each parameter is specified in points. The size of a volumetric scene is
immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:)

Sets a default width and height for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for windows created from a scene.

`height`

    

The default height for windows created from a scene.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this scene modifier to indicate a default initial size for a new window
that the system creates from a `Scene` declaration. For example, you can
request that new windows that a `WindowGroup` generates occupy 600 points in
the x-dimension and 400 points in the y-dimension:

The size that you specify acts only as a default for when the window first
appears. People can later resize the window using interface controls that the
system provides. Also, during state restoration, the system restores windows
to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s
inherent resizability in one or both dimensions, the system clamps the
affected dimension to keep it in range. You can configure the resizability of
a scene using the `windowResizability(_:)` modifier.

The default size modifier affects any scene type that creates windows in
macOS, namely:

  * `WindowGroup`

  * `Window`

  * `DocumentGroup`

  * `Settings`

If you want to specify the size input in terms of size instance, use
`defaultSize(_:)` instead.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:depth:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat,
        depth: CGFloat
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

    
    
    WindowGroup {
        ContentView()
    }
    .windowStyle(.volumetric)
    .defaultSize(width: 600, height: 400, depth: 600)
    

Each parameter is specified in points. The size of a volumetric scene is
immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(_:in:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        _ size: Size3D,
        in unit: UnitLength
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

`unit`

    

The unit of length the dimensions of the window are specified in.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in the unit you provide. The size of a volumetric
scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# defaultSize(width:height:depth:in:)

Sets a default size for a volumetric window.

visionOS 1.0+

    
    
    func defaultSize(
        width: CGFloat,
        height: CGFloat,
        depth: CGFloat,
        in unit: UnitLength
    ) -> some Scene
    

##  Parameters

`width`

    

The default width for the created window.

`height`

    

The default height for the created window.

`depth`

    

The default depth for the created volumetric window.

`unit`

    

The unit of length the dimensions of the window are specified in.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window
created from a `Scene` using `VolumetricWindowStyle`:

Each parameter is specified in the unit you provide. The size of a volumetric
scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.

`struct WindowResizability`

The resizability of a window.

Instance Method

# windowResizability(_:)

Sets the kind of resizability to use for a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func windowResizability(_ resizability: WindowResizability) -> some Scene
    

##  Parameters

`resizability`

    

The resizability to use for windows created by this scene.

## Return Value

A scene that uses the specified resizability strategy.

## Discussion

Use this scene modifier to apply a value of type `WindowResizability` to a
`Scene` that you define in your `App` declaration. The value that you specify
indicates the strategy the system uses to place minimum and maximum size
restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between
100 and 400 points in both dimensions by applying both a frame with those
constraints to the scene’s content, and the `contentSize` resizability to the
scene:

    
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .frame(
                        minWidth: 100, maxWidth: 400,
                        minHeight: 100, maxHeight: 400)
            }
            .windowResizability(.contentSize)
        }
    }
    

The default value for all scenes if you don’t apply the modifier is
`automatic`. With that strategy, `Settings` windows use the `contentSize`
strategy, while all others use `contentMinSize`.

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`struct WindowResizability`

The resizability of a window.

Structure

# WindowResizability

The resizability of a window.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct WindowResizability

## Overview

Use the `windowResizability(_:)` scene modifier to apply a value of this type
to a `Scene` that you define in your `App` declaration. The value that you
specify indicates the strategy the system uses to place minimum and maximum
size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between
100 and 400 points in both dimensions by applying both a frame with those
constraints to the scene’s content, and the `contentSize` resizability to the
scene:

The default value for all scenes if you don’t apply the modifier is
`automatic`. With that strategy, `Settings` windows use the `contentSize`
strategy, while all others use `contentMinSize`.

## Topics

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Positioning and sizing a window

Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

`func defaultPosition(UnitPoint) -> some Scene`

Sets a default position for a window.

`func defaultSize(CGSize) -> some Scene`

Sets a default size for a window.

`func defaultSize(Size3D) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat) -> some Scene`

Sets a default width and height for a window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some
Scene`

Sets a default size for a volumetric window.

`func defaultSize(Size3D, in: UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in:
UnitLength) -> some Scene`

Sets a default size for a volumetric window.

`func windowResizability(WindowResizability) -> some Scene`

Sets the kind of resizability to use for a window.



# WindowGroup

Initializer

# init(content:)

Creates a window group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

## See Also

### Creating a window group

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a text view title.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ title: Text,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a localized title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init<S>(S, content: () -> Content)`

Creates a window group with a title string.

Initializer

# init(_:content:)

Creates a window group with a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

The string to use for the title of the group.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Creating a window group

`init(content: () -> Content)`

Creates a window group.

`init(Text, content: () -> Content)`

Creates a window group with a text view title.

`init(LocalizedStringKey, content: () -> Content)`

Creates a window group with a localized title string.

Initializer

# init(id:content:)

Creates a window group with an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

## See Also

### Identifying a window group

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a text view title and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ title: Text,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a localized title string and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

The title key to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window group with a title string and an identifier.

Initializer

# init(_:id:content:)

Creates a window group with a title string and an identifier.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        id: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`content`

    

A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each
window in the group. The system uses the title to distinguish the window group
in the user interface, such as in the name of commands associated with the
group.

## See Also

### Identifying a window group

`init(id: String, content: () -> Content)`

Creates a window group with an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window group with a text view title and an identifier.

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window group with a localized title string and an identifier.

Initializer

# init(for:content:)

Creates a data-presenting window group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a localized title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:)

Creates a data-presenting window group with a text view title.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Creating a data-driven window group

`init<D, C>(for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string.

Available when `Content` conforms to `View`.

Initializer

# init(for:content:defaultValue:)

Creates a data-presenting window group with a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group using the given view as a template to form the content of
each window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a localized title string and a
default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a title string and a default
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a text view title and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(_:for:content:defaultValue:)

Creates a data-presenting window group with a text view title and a default
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Providing default data to a window group

`init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)`

Creates a data-presenting window group with a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string and a
default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, for: D.Type, content: (Binding<D>) -> C, defaultValue: () ->
D)`

Creates a data-presenting window group with a title string and a default
value.

Available when `Content` conforms to `View`.

Initializer

# init(id:for:content:)

Creates a data-presenting window group with an identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a localized title string and an
identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a title string and an identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a text view title and an
identifier.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:)

Creates a data-presenting window group with a text view title and an
identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        id: String,
        for type: D.Type,
        @ViewBuilder content: @escaping (Binding<D?>) -> C
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a data-driven window group

`init<D, C>(id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with an identifier.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content:
(Binding<D?>) -> C)`

Creates a data-presenting window group with a localized title string and an
identifier.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D?>) -> C)`

Creates a data-presenting window group with a title string and an identifier.

Available when `Content` conforms to `View`.

Initializer

# init(id:for:content:defaultValue:)

Creates a data-presenting window group with an identifier and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the given view as a template to form the content of each
window in the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ titleKey: LocalizedStringKey,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a title string, an identifier, and
a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S, D, C>(
        _ title: S,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the title of the group.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(Text, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

Available when `Content` conforms to `View`.

Initializer

# init(_:id:for:content:defaultValue:)

Creates a data-presenting window group with a text view title, an identifier,
and a default value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<D, C>(
        _ title: Text,
        id: String,
        for type: D.Type = D.self,
        @ViewBuilder content: @escaping (Binding<D>) -> C,
        defaultValue: @escaping () -> D
    ) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

The `Text` view to use for the group’s title.

`id`

    

A string that uniquely identifies the window group. Identifiers must be unique
among the window groups in your app.

`type`

    

The type of presented data this window group accepts.

`content`

    

A closure that creates the content for each instance of the group. The closure
receives a binding to the value that you pass into the `openWindow` action
when you open the window. SwiftUI automatically persists and restores the
value of this binding as part of the state restoration process.

`defaultValue`

    

A closure that returns a default value to present. SwiftUI calls this closure
when it has no data to provide, like when someone opens a new window from the
File > New Window menu item.

## Discussion

The window group uses the specified content as a template to create each
window in the group.

The system uses the title to distinguish the window group in the user
interface, such as in the name of commands associated with the group.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

SwiftUI creates a window from the group when you present a value of the
specified type using the `openWindow` action.

## See Also

### Identifying a window group that has default data

`init<D, C>(id: String, for: D.Type, content: (Binding<D>) -> C, defaultValue:
() -> D)`

Creates a data-presenting window group with an identifier and a default value.

Available when `Content` conforms to `View`.

`init<D, C>(LocalizedStringKey, id: String, for: D.Type, content: (Binding<D>)
-> C, defaultValue: () -> D)`

Creates a data-presenting window group with a localized title string, an
identifier, and a default value.

Available when `Content` conforms to `View`.

`init<S, D, C>(S, id: String, for: D.Type, content: (Binding<D>) -> C,
defaultValue: () -> D)`

Creates a data-presenting window group with a title string, an identifier, and
a default value.

Available when `Content` conforms to `View`.

Structure

# PresentedWindowContent

A view that represents the content of a presented window.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct PresentedWindowContent<Data, Content> where Data : Decodable, Data : Encodable, Data : Hashable, Content : View

## Overview

You don’t create this type directly. `WindowGroup` creates values for you.

## Relationships

### Conforms To

  * `View`



# Widget

Instance Property

# body

The content and behavior of the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## Discussion

For any widgets that you create, provide a computed `body` property that
defines the widget as a composition of SwiftUI views.

Swift infers the widget’s `Body` associated type based on the contents of the
`body` property.

## See Also

### Implementing a widget

`associatedtype Body : WidgetConfiguration`

The type of configuration representing the content of the widget.

**Required**

Associated Type

# Body

The type of configuration representing the content of the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    associatedtype Body : WidgetConfiguration

**Required**

## Discussion

When you create a custom widget, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing a widget

`var body: Self.Body`

The content and behavior of the widget.

**Required**

Initializer

# init()

Creates a widget using `body` as its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()

**Required**

## See Also

### Running a widget

`static func main()`

Initializes and runs the widget.

Type Method

# main()

Initializes and runs the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func main()

## Overview

Because you precede your `Widget` conformer’s declaration with the @main
attribute, the system calls your widget’s `main()` method to launch the
widget. SwiftUI provides a default implementation of the method that manages
the launch process in a platform-appropriate way.

## See Also

### Running a widget

`init()`

Creates a widget using `body` as its content.

**Required**



# WKUserNotificationHostingController

Initializer

# init()

Creates a notification hosting controller object that you can use to implement
your notification interfaces using SwiftUI views.

watchOS 6.0+

    
    
    @MainActor
    override dynamic init()

Instance Property

# body

The root view of the view hierarchy to display for your notification
interface.

watchOS 6.0+

    
    
    @MainActor
    var body: Body { get }

## Discussion

Override this property and return the root view of your SwiftUI view hierarchy
from your implementation. If you don’t override this property, accessing the
default implementation triggers an exception.

Type Property

# coalescedDescriptionFormat

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

watchOS 7.0+

    
    
    @MainActor
    class var coalescedDescriptionFormat: String? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# isInteractive

If the notification should accept user input.

watchOS 7.0+

    
    
    @MainActor
    class var isInteractive: Bool { get }

## Discussion

Default value is `false`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# sashColor

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var sashColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# subtitleColor

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var subtitleColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# titleColor

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var titleColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# wantsSashBlur

If the sash should include a blur over the background.

watchOS 7.0+

    
    
    @MainActor
    class var wantsSashBlur: Bool { get }

## Discussion

Default value is `false`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.



# WindowMenuBarExtraStyle

Initializer

# init()

Creates a window menu bar extra style.

macOS 13.0+

    
    
    init()



# WidgetBundleBuilder

Type Method

# buildBlock()

Builds an empty Widget from a block containing no statements, `{ }`.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock() -> some Widget
    

## See Also

### Bundling widgets

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:)

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> some Widget where Content : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> some Widget where C0 : Widget, C1 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget, C8 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> some Widget where C0 : Widget, C1 : Widget, C2 : Widget, C3 : Widget, C4 : Widget, C5 : Widget, C6 : Widget, C7 : Widget, C8 : Widget, C9 : Widget
    

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildLimitedAvailability(_:)

Processes widget content for a conditional compiler-control statement that
performs an availability check.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildLimitedAvailability(_ widget: some Widget) -> any Widget & _LimitedAvailabilityWidgetMarker

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

Type Method

# buildOptional(_:)

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func buildOptional(_ widget: (any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget
    

## Discussion

Conditional statements in a `WidgetBundleBuilder` can contain an `if`
statement but not an `else` statement, and the condition can only perform a
compiler check for availability, like in the following code:

## See Also

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.



# WidgetConfiguration

Instance Property

# body

The content and behavior of this widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## See Also

### Implementing a widget

`associatedtype Body : WidgetConfiguration`

The type of widget configuration representing the body of this configuration.

**Required**

Associated Type

# Body

The type of widget configuration representing the body of this configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    associatedtype Body : WidgetConfiguration

**Required**

## Discussion

When you create a custom widget, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing a widget

`var body: Self.Body`

The content and behavior of this widget.

**Required**

Instance Method

# configurationDisplayName(_:)

Sets the name shown for a widget when a user adds or edits it using the
specified string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName<S>(_ displayName: S) -> some WidgetConfiguration where S : StringProtocol
    

##  Parameters

`displayName`

    

A string describing the widget.

## Return Value

A widget configuration that includes a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

Instance Method

# configurationDisplayName(_:)

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName(_ displayName: Text) -> some WidgetConfiguration
    

##  Parameters

`displayName`

    

A text view containing a localized string to display.

## Return Value

A widget configuration with a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

Instance Method

# configurationDisplayName(_:)

Sets the localized name shown for a widget when a user adds or edits the
widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func configurationDisplayName(_ displayNameKey: LocalizedStringKey) -> some WidgetConfiguration
    

##  Parameters

`displayName`

    

The key for the localized name to display.

## Return Value

A widget configuration that includes a descriptive name for the widget.

## See Also

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

Instance Method

# description(_:)

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description(_ description: Text) -> some WidgetConfiguration
    

##  Parameters

`description`

    

A text view containing a localized string to display.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

Instance Method

# description(_:)

Sets the description shown for a widget when a user adds or edits it using the
specified string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol
    

##  Parameters

`displayName`

    

A string describing the widget.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

Instance Method

# description(_:)

Sets the localized description shown for a widget when a user adds or edits
the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func description(_ descriptionKey: LocalizedStringKey) -> some WidgetConfiguration
    

##  Parameters

`descriptionKey`

    

The key for the localized description to display.

## Return Value

A widget configuration with a description of the widget.

## See Also

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

Instance Method

# supportedFamilies(_:)

Sets the sizes that a widget supports.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func supportedFamilies(_ families: [WidgetFamily]) -> some WidgetConfiguration
    

##  Parameters

`families`

    

The set of sizes the widget supports.

## Return Value

A widget configuration that supports the sizes you specify.

## See Also

### Setting the appearance

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# contentMarginsDisabled()

Disable default content margins.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func contentMarginsDisabled() -> some WidgetConfiguration
    

## Return Value

A modified widget configuration that doesn’t use default content margins.

## Discussion

When you disable content margins for a widget, the system doesn’t
automatically add margins around the widget’s content, and you are responsible
for specifying margins and padding around your widget content for each
context. To specify custom margins, use `widgetContentMargins` in combination
with `View/padding(_)` to selectively or partially apply the default content
margins.

This modifier has no effect on operation system versions prior to iOS 17,
watchOS 10, or macOS 14.

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# disfavoredLocations(_:for:)

Sets the disfavored locations for a widget.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func disfavoredLocations(
        _ locations: [WidgetLocation],
        for families: [WidgetFamily]
    ) -> some WidgetConfiguration
    

##  Parameters

`locations`

    

An array of disfavored locations for a widget.

`families`

    

The families you want to mark as disfavored in the given locations.

## Discussion

A widget can appear in different contexts on different platforms. For example,
a small system widget appears by default on the Home Screen and in Today View
on iPhone, on the iPad Lock Screen, and so on. This gives more people
opportunity to view data and functionality that your widget provides. However,
some widgets may not work well in a location. For example, a widget that
heavily relies on high-resolution photos and background colors for its
functionality may not work well on the Lock Screen, where the system applies a
vibrant treatment to the widget. To tell the system that the widget gallery
should show a widget in the “Other” section of the widget gallery for a
specific context, use the `.disfavoredLocations` modifier.

The following code snippet tells the system to show the small system family
widget in the “Other” section of the widget gallery for the disfavored
`WidgetLocation/lockScreen` and `WidgetLocation/homeScreen` locations.

You can use subsequent calls to `disfavoredLocations(_:families:)` to join
them and set disfavored locations for different families:

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

Instance Method

# containerBackgroundRemovable(_:)

A modifier that marks the background of a widget as removable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func containerBackgroundRemovable(_ isRemovable: Bool = true) -> some WidgetConfiguration
    

##  Parameters

`isRemovable`

    

If `true`, the widget supports removal of the container background in contexts
that prefer no backgrounds. If `false`, the system doesn’t remove the
background.

## Return Value

A modified widget configuration.

## Discussion

In most cases, mark the background container of a widget as removable to allow
people to place the widget in as many contexts as possible. If you mark the
background as nonremovable, the widget becomes ineligible in various contexts
that require a removable background. For example, a small widget without a
removable background doesn’t appear in the widget gallery on the iPad Lock
Screen.

If you mark a background as nonremovable, the system always displays the
background container of the widget. Note that the background may render
differently; for example, it can appear faded or desaturated.

This modifier has no effect on operation system versions prior to iOS 17,
watchOS 10, or macOS 14.

## See Also

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

Instance Method

# backgroundTask(_:action:)

Runs the given action when the system provides a background task.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func backgroundTask<D, R>(
        _ task: BackgroundTask<D, R>,
        action: @escaping (D) async -> R
    ) -> some WidgetConfiguration where D : Sendable, R : Sendable
    

##  Parameters

`task`

    

The type of task the action responds to.

`action`

    

The closure that is called when the system provides a task matching the
provided task.

## Discussion

When the system wakes your app or extension for one or more background tasks,
it will call any actions associated with matching tasks. When your async
actions return, the system will put your app back into a suspended state. In
Widget Extensions, this modifier can be used to handle URL Session background
tasks with `urlSession`.

## See Also

### Managing background tasks

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

Instance Method

# onBackgroundURLSessionEvents(matching:_:)

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func onBackgroundURLSessionEvents(
        matching matchingBlock: ((String) -> Bool)? = nil,
        _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void
    ) -> some WidgetConfiguration
    

##  Parameters

`matching`

    

A closure that takes a string identifier and returns a Boolean value
indicating whether to perform the action.

`urlSessionEvent`

    

A closure that takes a string parameter called `identifier` and a closure
called `completion`.

## Return Value

A widget that triggers `urlSessionEvent` when events are generated for a
`URLSession` with the specified identifier.

## Discussion

When a widget initiates a background network request, the system delivers
events related to the request directly to the widget extension instead of the
containing app. To process the events, do the following:

  1. Use the `identifier` parameter to determine if a corresponding `URLSession` object exists. If the system hasn’t terminated your widget extension, maintain a reference to the same `URLSession` object you used for the original background network request. If the system terminated your widget extension, use the identifier to create a new `URLSession` object so it can receive the events. You might consider lazily initializing, and caching, the `URLSession` objects in a central location so that your code works regardless of whether your extension remains active, is suspended, or is terminated.

  2. Store a reference to the `completion` closure to invoke it after the system delivers all events.

  3. After the system calls the `URLSession` delegate’s `urlSessionDidFinishEvents(forBackgroundURLSession:)` method, invoke the `completion` closure.

## See Also

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

Instance Method

# onBackgroundURLSessionEvents(matching:_:)

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func onBackgroundURLSessionEvents(
        matching matchingString: String,
        _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void
    ) -> some WidgetConfiguration
    

##  Parameters

`matching`

    

The identifier of a URL session to monitor for events.

`urlSessionEvent`

    

A closure that takes a string identifier and a closure called `completion` as
parameters.

## Return Value

A widget that triggers `urlSessionEvent` when events are generated for a
`URLSession` with the specified identifier.

## Discussion

When a widget initiates a background network request, the system delivers
events related to the request directly to the widget extension instead of the
containing app. To process the events, do the following:

  1. Use the `matching` parameter to determine if a corresponding `URLSession` object exists. If the system hasn’t terminated your widget extension, maintain a reference to the same `URLSession` object you used for the original background network request. If the system terminated your widget extension, use the identifier to create a new `URLSession` object so it can receive the events. You might consider lazily initializing, and caching, the `URLSession` objects in a central location so that your code works regardless of whether your extension remains active, is suspended, or is terminated.

  2. Store a reference to the `completion` closure of `urlSessionEvent` to invoke it after the system delivers all events.

  3. After the system calls the `URLSession` delegate’s `urlSessionDidFinishEvents(forBackgroundURLSession:)` method, invoke the `completion` closure.

## See Also

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.



# Window

Initializer

# init(_:id:content:)

Creates a window with a localized title and an identifier.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

A localized string key to use for the window’s title in system menus and in
the window’s title bar. Provide a title that describes the purpose of the
window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

## See Also

### Creating a window

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

Initializer

# init(_:id:content:)

Creates a window with a title string and an identifier.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        id: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

A string to use for the window’s title in system menus and in the window’s
title bar. Provide a title that describes the purpose of the window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

## See Also

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

Initializer

# init(_:id:content:)

Creates a window with a title and an identifier.

macOS 13.0+

    
    
    init(
        _ title: Text,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the window’s title in system menus and in the
window’s title bar. Provide a title that describes the purpose of the window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.



# WKInterfaceObjectRepresentable

Instance Method

# makeWKInterfaceObject(context:)

Creates a WatchKit interface object and configures its initial state.

watchOS 6.0+

    
    
    @MainActor
    func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your interface object configured with the provided information.

## Discussion

You must implement this method and use it to create your interface object.
Configure the object using your app’s current data and contents of the
`context` parameter. The system calls this method only once, when it creates
your interface object for the first time. For all subsequent updates, the
system calls the `updateWKInterfaceObject(_:context:)` method.

## See Also

### Creating and updating the interface object

`func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

` typealias Context`

Instance Method

# updateWKInterfaceObject(_:context:)

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

watchOS 6.0+

    
    
    @MainActor
    func updateWKInterfaceObject(
        _ wkInterfaceObject: Self.WKInterfaceObjectType,
        context: Self.Context
    )

**Required**

##  Parameters

`wkInterfaceObject`

    

Your custom interface object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding interface object. Use this method to update the
configuration of your object to match the new state information provided in
the `context` parameter.

## See Also

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` typealias Context`

Type Alias

# WKInterfaceObjectRepresentable.Context

watchOS 6.0+

    
    
    typealias Context = WKInterfaceObjectRepresentableContext<Self>

## See Also

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

Type Method

# dismantleWKInterfaceObject(_:coordinator:)

Cleans up the presented WatchKit interface object (and its coordinator) in
anticipation of their removal.

watchOS 6.0+

    
    
    @MainActor
    static func dismantleWKInterfaceObject(
        _ wkInterfaceObject: Self.WKInterfaceObjectType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`wkInterfaceObject`

    

Your custom interface object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
interface object. For example, you might use this method to remove observers
or update other parts of your SwiftUI interface.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

`static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType,
coordinator: Self.Coordinator)`

Cleans up the presented interface object (and coordinator) in anticipation of
their removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

watchOS 6.0+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your interface object might affect other
parts of your app. In your implementation, create a custom Swift instance that
can communicate with other parts of your interface. For example, you might
provide an instance that binds its variables to SwiftUI properties, causing
the two to remain synchronized. If your interface object doesn’t interact with
other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeWKInterfaceObject(context:)`
method. The system provides your coordinator either directly or as part of a
context structure when calling the other methods of your representable
instance.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**

` associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

Associated Type

# Coordinator

A type to coordinate with the WatchKit interface object.

watchOS 6.0+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

Associated Type

# WKInterfaceObjectType

The type of WatchKit interface object to be presented.

watchOS 6.0+

    
    
    associatedtype WKInterfaceObjectType : WKInterfaceObject

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**



# WKExtensionDelegateAdaptor

Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` protocol.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling upon it to
handle extension delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the `Environment`,
make sure the delegate class also conforms to the `ObservableObject` protocol.
That causes SwiftUI to invoke the `init(_:)` initializer rather than this one.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` and `ObservableObject` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle extension delegate callbacks.

SwiftUI invokes this method when your extension delegate conforms to the
`ObservableObject` protocol. In this case, SwiftUI automatically places the
delegate in the `Environment`. You can access such a delegate from any scene
or view in your app using the `EnvironmentObject` property wrapper:

If your delegate isn’t an observable object, SwiftUI invokes the `init(_:)`
initializer rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor using an observable delegate.

watchOS 10.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` and `Observable` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle extension delegate callbacks.

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

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

Instance Property

# projectedValue

A projection of the observed object that provides bindings to its properties.

watchOS 7.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

## Discussion

Use the projected value to get a binding to a value that the delegate
publishes. Access the projected value by prefixing the name of the delegate
instance with a dollar sign (`$`). For example, you might publish a Boolean
value in your extension delegate:

If you declare the delegate in your `App` using the
`WKExtensionDelegateAdaptor` property wrapper, you can get the delegate that
SwiftUI instantiates from the environment and access a binding to its
published values from any view in your extension:

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying delegate.

Instance Property

# wrappedValue

The underlying delegate.

watchOS 7.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.



# WKNotificationScene

Initializer

# init(controller:category:)

Creates a scene that appears in response to receiving a specific category of
remote or local notifications.

watchOS 7.0+

    
    
    init(
        controller: Controller.Type = Controller.self,
        category: String
    )

##  Parameters

`controller`

    

The type of `WKUserNotificationHostingController` to display upon receipt of
the specified notification category.

`category`

    

The category of notifications to listen for.

## Discussion

Use a watch notification instance to add support for one or more Apple Watch
notification scenes that appear on receipt of the local or remote notification
categories you specify. The example below, adds two notification scenes to the
app declaration:

Each `WKNotificationScene` declaration references a
`WKUserNotificationHostingController` and a category string that you provide.
The hosting controller displays your notification’s content view upon receipt
of a local or a PushKit notification. The category string you specify
corresponds to the category name in the notification’s dictionary and
describes a specific notification that contains the content displayed by the
notification view.



# WidgetBundle

Instance Property

# body

Declares the group of widgets that an app supports.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @WidgetBundleBuilder
    var body: Self.Body { get }

**Required**

## Discussion

The order that the widgets appear in this property determines the order they
are shown to the user when adding a widget. The following example shows how to
use a widget bundle builder to define a body showing a game status widget
first and a character detail widget second:

## See Also

### Implementing a widget bundle

`associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

Associated Type

# Body

The type of widget that represents the content of the bundle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    associatedtype Body : Widget

**Required**

## Discussion

When you support more than one widget, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

Structure

# WidgetBundleBuilder

A custom attribute that constructs a widget bundle’s body.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @resultBuilder
    struct WidgetBundleBuilder

## Overview

Use the `@WidgetBundleBuilder` attribute to group multiple widgets listed in
the `body` property of a widget bundle. For example, the following code
defines a widget bundle that consists of two widgets.

## Topics

### Bundling widgets

`static func buildBlock() -> some Widget`

Builds an empty Widget from a block containing no statements, `{ }`.

`static func buildBlock<Content>(Content) -> some Widget`

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`)
through unmodified.

`static func buildBlock<C0, C1>(C0, C1) -> some Widget`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Widget`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Widget`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Widget`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

`static func buildLimitedAvailability(some Widget) -> any Widget &
_LimitedAvailabilityWidgetMarker`

Processes widget content for a conditional compiler-control statement that
performs an availability check.

`static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?)
-> some Widget`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

## See Also

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

Initializer

# init()

Creates a widget bundle using the bundle’s body as its content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()

**Required**

## See Also

### Running a widget bundle

`static func main()`

Initializes and runs the widget bundle.

Type Method

# main()

Initializes and runs the widget bundle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func main()

## Overview

Because you precede your `WidgetBundle` conformer’s declaration with the @main
attribute, the system calls your widget bundle’s `main()` method to launch the
widget bundle. SwiftUI provides a default implementation of the method that
manages the launch process in a platform-appropriate way.

## See Also

### Running a widget bundle

`init()`

Creates a widget bundle using the bundle’s body as its content.

**Required**



# WatchKit integration

Class

# WKHostingController

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

watchOS 6.0+

    
    
    @MainActor
    class WKHostingController<Body> where Body : View

## Overview

A `WKHostingController` presents and manages your app’s main interface using
SwiftUI views. You must subclass `WKHostingController` and override the `body`
property to provide the set of SwiftUI views you want to display. Display the
content of your hosting controller as you would any other
`WKInterfaceController` object. For example, you can include it as one of your
app’s root interface controllers, or present it modally.

## Topics

### Creating a hosting controller object

`init()`

Creates a hosting controller object that you can use to implement your app’s
main interface using SwiftUI views

### Getting the root view

`var body: Body`

The root view of the view hierarchy to display for your interface controller.

### Updating the root view

`func updateBodyIfNeeded()`

Updates the interface controller’s set of views immediately, if updates are
pending.

`func setNeedsBodyUpdate()`

Invalidates the current SwiftUI views and triggers an update during the next
cycle.

## Relationships

### Inherits From

  * `WKInterfaceController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSObjectProtocol`

## See Also

### Displaying SwiftUI views in WatchKit

`class WKUserNotificationHostingController`

A WatchKit user notification interface controller that hosts a SwiftUI view
hierarchy.

Class

# WKUserNotificationHostingController

A WatchKit user notification interface controller that hosts a SwiftUI view
hierarchy.

watchOS 6.0+

    
    
    @MainActor
    class WKUserNotificationHostingController<Body> where Body : View

## Overview

A `WKUserNotificationHostingController` presents and manages your app’s
notification interface using SwiftUI views. You must subclass
`WKUserNotificationHostingController` and override the `body` property to
provide the set of SwiftUI views you want to display. In the storyboard of
your watch app, specify the name of your custom class for your dynamic
interactive interface.

## Topics

### Creating a hosting controller object

`init()`

Creates a notification hosting controller object that you can use to implement
your notification interfaces using SwiftUI views.

### Getting the root view

`var body: Body`

The root view of the view hierarchy to display for your notification
interface.

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

## Relationships

### Inherits From

  * `WKUserNotificationInterfaceController`

### Conforms To

  * `CVarArg`
  * `CustomDebugStringConvertible`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `NSObjectProtocol`

## See Also

### Displaying SwiftUI views in WatchKit

`class WKHostingController`

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

Protocol

# WKInterfaceObjectRepresentable

A view that represents a WatchKit interface object.

watchOS 6.0+

    
    
    protocol WKInterfaceObjectRepresentable : View where Self.Body == Never

## Overview

Use a `WKInterfaceObjectRepresentable` instance to create and manage a
`WKInterfaceObject` in your SwiftUI interface. Adopt this protocol in one of
your app’s custom instances, and use its methods to create, update, and tear
down your interface object. The creation and update processes parallel the
behavior of SwiftUI views, and you use them to configure your interface object
with your app’s current state information. Use the teardown process to remove
your interface object cleanly from your SwiftUI. For example, you might use
the teardown process to notify other parts of your app that the interface
object is disappearing.

To add your interface object into your SwiftUI interface, create your
`WKInterfaceObjectRepresentable` instance and add it to your SwiftUI
interface. The system calls the methods of your representable instance at
appropriate times to create and update the interface object.

The system doesn’t automatically communicate changes occurring within your
interface object to other parts of your SwiftUI interface. When you want your
interface object to coordinate with other SwiftUI views, you must provide a
`Coordinator` instance to facilitate those interactions. For example, you use
a coordinator to forward target-action and delegate messages from your
interface object to any SwiftUI views.

## Topics

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

` typealias Context`

### Cleaning up the interface object

`static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType,
coordinator: Self.Coordinator)`

Cleans up the presented WatchKit interface object (and its coordinator) in
anticipation of their removal.

**Required** Default implementation provided.

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**

` associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

## Relationships

### Inherits From

  * `View`

## See Also

### Adding WatchKit views to SwiftUI view hierarchies

`struct WKInterfaceObjectRepresentableContext`

Contextual information about the state of the system that you use to create
and update your WatchKit interface object.

Structure

# WKInterfaceObjectRepresentableContext

Contextual information about the state of the system that you use to create
and update your WatchKit interface object.

watchOS 6.0+

    
    
    @MainActor
    struct WKInterfaceObjectRepresentableContext<Representable> where Representable : WKInterfaceObjectRepresentable

## Overview

A `WKInterfaceObjectRepresentableContext` structure contains details about the
current state of the system. When creating and updating your interface
objects, the system creates one of these structures and passes it to the
appropriate method of your custom `WKInterfaceObjectRepresentable` instance.
Use the information in this structure to configure your object. Don’t create
this structure yourself.

## Topics

### Coordinating interactions

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

### Adding WatchKit views to SwiftUI view hierarchies

`protocol WKInterfaceObjectRepresentable`

A view that represents a WatchKit interface object.



# WindowStyle

Type Property

# automatic

The default window style.

macOS 11.0+  visionOS 1.0+

    
    
    static var automatic: DefaultWindowStyle { get }

Available when `Self` is `DefaultWindowStyle`.

## See Also

### Getting built-in window styles

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# hiddenTitleBar

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

macOS 11.0+

    
    
    static var hiddenTitleBar: HiddenTitleBarWindowStyle { get }

Available when `Self` is `HiddenTitleBarWindowStyle`.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# plain

The plain window style.

visionOS 1.0+

    
    
    static var plain: PlainWindowStyle { get }

Available when `Self` is `PlainWindowStyle`.

## Discussion

Unlike `automatic`, a plain window does not receive a glass background in
visionOS. Use this style if you want more control over how glass is used in
your window.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# titleBar

A window style which displays the title bar section of the window.

macOS 11.0+

    
    
    static var titleBar: TitleBarWindowStyle { get }

Available when `Self` is `TitleBarWindowStyle`.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var volumetric: VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Available when `Self` is `VolumetricWindowStyle`.

Type Property

# volumetric

A window style that creates a 3D volumetric window.

visionOS 1.0+

    
    
    static var volumetric: VolumetricWindowStyle { get }

Available when `Self` is `VolumetricWindowStyle`.

## Discussion

Use a volumetric window — or a _volume_ — to display 3D content within a
bounded region. For example, Hello World uses a volume to present a `Globe`
model that people can pick up and move around the Shared Space using the
window bar:

A volume enables someone to view content from all angles, unlike other windows
which fade out as people move around the window. Also unlike other windows, a
volume uses fixed scale, which means that objects in the volume appear smaller
when the volume is farther away, like real objects would. For a comparison of
fixed and dynamic scale, see Spatial layout in the Human Interface Guidelines.

You can specify a size for the volume using one of the default size scene
modifiers, like `defaultSize(width:height:depth:in:)`. Because volumes use
fixed scale, it’s typically convenient to specify a size in physical units —
like meters, as the above code demonstrates. People can’t change the size of
the volume after it appears.

For design guidance, see Windows in the Human Interface Guidelines. If you
want to place 3D objects arbitrarily throughout the Shared Space or in a Full
Space, use an `ImmersiveSpace` instead.

## See Also

### Getting built-in window styles

`static var automatic: DefaultWindowStyle`

The default window style.

Available when `Self` is `DefaultWindowStyle`.

`static var hiddenTitleBar: HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

Available when `Self` is `HiddenTitleBarWindowStyle`.

`static var plain: PlainWindowStyle`

The plain window style.

Available when `Self` is `PlainWindowStyle`.

`static var titleBar: TitleBarWindowStyle`

A window style which displays the title bar section of the window.

Available when `Self` is `TitleBarWindowStyle`.

Structure

# DefaultWindowStyle

The default window style.

macOS 11.0+  visionOS 1.0+

    
    
    struct DefaultWindowStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# HiddenTitleBarWindowStyle

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

macOS 11.0+

    
    
    struct HiddenTitleBarWindowStyle

## Overview

You can also use `hiddenTitleBar` to construct this style.

## Topics

### Creating the window style

`init()`

Creates a hidden title bar window style.

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# PlainWindowStyle

The plain window style.

visionOS 1.0+

    
    
    struct PlainWindowStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# TitleBarWindowStyle

A window style which displays the title bar section of the window.

macOS 11.0+

    
    
    struct TitleBarWindowStyle

## Overview

You can also use `titleBar` to construct this style.

## Topics

### Creating the window style

`init()`

Creates a title bar window style.

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct VolumetricWindowStyle`

A window style that creates a 3D volumetric window.

Structure

# VolumetricWindowStyle

A window style that creates a 3D volumetric window.

visionOS 1.0+

    
    
    struct VolumetricWindowStyle

## Overview

Use `volumetric` to construct this style:

## Topics

### Creating the window style

`init()`

## Relationships

### Conforms To

  * `WindowStyle`

## See Also

### Supporting types

`struct DefaultWindowStyle`

The default window style.

`struct HiddenTitleBarWindowStyle`

A window style which hides both the window’s title and the backing of the
titlebar area, allowing more of the window’s content to show.

`struct PlainWindowStyle`

The plain window style.

`struct TitleBarWindowStyle`

A window style which displays the title bar section of the window.



