Instance Method

# dropEntered(info:)

Tells the delegate a validated drop has entered the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropEntered(info: DropInfo)

**Required** Default implementation provided.

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

## See Also

### Receiving drop information

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

Instance Method

# dropExited(info:)

Tells the delegate a validated drop operation has exited the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropExited(info: DropInfo)

**Required** Default implementation provided.

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

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

Instance Method

# dropUpdated(info:)

Tells the delegate that a validated drop moved inside the modified view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func dropUpdated(info: DropInfo) -> DropProposal?

**Required** Default implementation provided.

## Discussion

Use this method to return a drop proposal containing the operation the
delegate intends to perform at the drop `location`. The default implementation
of this method returns `nil`, which tells the drop to use the last valid
returned value or else `DropOperation.copy`.

## Default Implementations

### DropDelegate Implementations

`func dropUpdated(info: DropInfo) -> DropProposal?`

Tells the delegate that a validated drop moved inside the modified view.

## See Also

### Receiving drop information

`func dropEntered(info: DropInfo)`

Tells the delegate a validated drop has entered the modified view.

**Required** Default implementation provided.

`func dropExited(info: DropInfo)`

Tells the delegate a validated drop operation has exited the modified view.

**Required** Default implementation provided.

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

**Required** Default implementation provided.

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# validateDrop(info:)

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func validateDrop(info: DropInfo) -> Bool

**Required** Default implementation provided.

## Discussion

Specify the expected types when you apply the drop modifier to the view. The
default implementation returns `true`.

## Default Implementations

### DropDelegate Implementations

`func validateDrop(info: DropInfo) -> Bool`

Tells the delegate that a drop containing items conforming to one of the
expected types entered a view that accepts drops.

## See Also

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

`func performDrop(info: DropInfo) -> Bool`

Tells the delegate it can request the item provider data from the given
information.

**Required**

Instance Method

# performDrop(info:)

Tells the delegate it can request the item provider data from the given
information.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    @MainActor
    func performDrop(info: DropInfo) -> Bool

**Required**

## Return Value

A Boolean that is `true` if the drop was successful, `false` otherwise.

## Discussion

Incorporate the received data into your app’s data model as appropriate.

## See Also

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

