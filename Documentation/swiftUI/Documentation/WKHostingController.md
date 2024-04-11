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

