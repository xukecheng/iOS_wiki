Instance Method

# draggable(_:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single instance or a value conforming to
`Transferable` that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag
and drop to this view. When a drag operation begins, a rendering of this view
is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# draggable(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<V, T>(
        _ payload: @autoclosure @escaping () -> T,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View, T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single class instance or a value conforming to
`Transferable` that represents the draggable data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:preview:)` modifier adds the appropriate gestures
for drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# dropDestination(for:action:isTargeted:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], CGPoint) -> Bool,
        isTargeted: @escaping (Bool) -> Void = { _ in }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the dropped models.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items. The second parameter
contains the drop location in this view’s coordinate space. Return `true` if
the drop operation was successful; otherwise, return `false`.

`isTargeted`

    

A closure that is called when a drag and drop operation enters or exits the
drop target area. The received value is `true` when the cursor is inside the
area, and `false` when the cursor is outside.

## Return Value

A view that provides a drop destination for a drag operation of the specified
type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file
promises.

The drop destination is the same size and position as this view.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

Instance Method

# itemProvider(_:)

Provides a closure that vends the drag representation to be used for a
particular data element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View
    

## See Also

### Moving items using item providers

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func onDrag<V>(
        _ data: @escaping () -> NSItemProvider,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag-and- drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for
drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:)

Activates this view as the source of a drag and drop operation.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and
drop to this view. When a drag operation begins, a rendering of this view is
generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag-and-drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider], CGPoint) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. The second parameter contains the drop location in
this view’s coordinate space. Return `true` if the drop operation was
successful; otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:delegate:)

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        delegate: any DropDelegate
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`delegate`

    

A type that conforms to the `DropDelegate` protocol. You have comprehensive
control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Protocol

# DropDelegate

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    protocol DropDelegate

## Overview

The `DropDelegate` protocol provides a comprehensive and flexible way to
interact with a drop operation. Specify a drop delegate when you modify a view
to accept drops with the `onDrop(of:delegate:)` method.

Alternatively, for simple drop cases that don’t require the full functionality
of a drop delegate, you can modify a view to accept drops using the
`onDrop(of:isTargeted:perform:)` or the `onDrop(of:isTargeted:perform:)`
method. These methods handle the drop using a closure you provide as part of
the modifier.

## Topics

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Structure

# DropProposal

The behavior of a drop.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct DropProposal

## Topics

### Creating a drop proposal

`init(operation: DropOperation)`

`let operation: DropOperation`

The drop operation that the drop proposes to perform.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Enumeration

# DropOperation

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    enum DropOperation

## Topics

### Getting operation types

`case cancel`

Cancel the drag operation and transfer no data.

`case copy`

Copy the data to the modified view.

`case forbidden`

The drop activity is not allowed at this time or location.

`case move`

Move the data represented by the drag items instead of copying it.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`struct DropInfo`

The current state of a drop.

Structure

# DropInfo

The current state of a drop.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct DropInfo

## Topics

### Getting the drop location

`var location: CGPoint`

The location of the drag in the coordinate space of the drop view.

### Checking for items

`func hasItemsConforming(to: [UTType]) -> Bool`

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

`func itemProviders(for: [UTType]) -> [NSItemProvider]`

Finds item providers that conform to at least one of the specified uniform
type identifiers.

### Deprecated symbols

`func hasItemsConforming(to: [String]) -> Bool`

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

Deprecated

`func itemProviders(for: [String]) -> [NSItemProvider]`

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

Deprecated

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

Instance Method

# springLoadingBehavior(_:)

Sets the spring loading behavior this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func springLoadingBehavior(_ behavior: SpringLoadingBehavior) -> some View
    

##  Parameters

`behavior`

    

Whether spring loading is enabled or not. If unspecified, the default behavior
is `.automatic.`

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

Unlike `disabled(_:)`, this modifier overrides the value set by an ancestor
view rather than being unioned with it. For example, the below button would
allow spring loading:

## See Also

### Configuring spring loading

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

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

Structure

# SpringLoadingBehavior

The options for controlling the spring loading behavior of views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SpringLoadingBehavior

## Overview

Use values of this type with the `springLoadingBehavior(_:)` modifier.

## Topics

### Getting the behaviors

`static let automatic: SpringLoadingBehavior`

The automatic spring loading behavior.

`static let enabled: SpringLoadingBehavior`

Spring loaded interactions will be enabled for applicable views.

`static let disabled: SpringLoadingBehavior`

Spring loaded interactions will be disabled for applicable views.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring spring loading

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

