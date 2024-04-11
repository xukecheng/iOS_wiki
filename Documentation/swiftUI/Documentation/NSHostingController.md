Initializer

# init(rootView:)

Creates a hosting controller object that wraps the specified SwiftUI view.

macOS 10.15+

    
    
    @MainActor
    init(rootView: Content)

##  Parameters

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using the
hosting view controller.

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

macOS 10.15+

    
    
    @MainActor
    init?(
        coder: NSCoder,
        rootView: Content
    )

##  Parameters

`coder`

    

The decoder to use during initialization.

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using this
view controller.

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

macOS 10.15+

    
    
    @MainActor
    required dynamic init?(coder: NSCoder)

##  Parameters

`coder`

    

The decoder to use during initialization.

## Discussion

The default implementation of this method throws an exception. To create your
view controller from an archive, override this method and initialize the
superclass using the `init(coder:rootView:)` method instead.

## See Also

### Creating a hosting controller object

`init(rootView: Content)`

Creates a hosting controller object that wraps the specified SwiftUI view.

`init?(coder: NSCoder, rootView: Content)`

Creates a hosting controller object from an archive and the specified SwiftUI
view.

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this view controller.

macOS 10.15+

    
    
    @MainActor
    var rootView: Content { get set }

## See Also

### Getting the root view

`var identifier: NSUserInterfaceItemIdentifier?`

Instance Property

# identifier

macOS 10.15+

    
    
    @MainActor
    override dynamic var identifier: NSUserInterfaceItemIdentifier? { get set }

## See Also

### Getting the root view

`var rootView: Content`

The root view of the SwiftUI view hierarchy managed by this view controller.

Instance Method

# sizeThatFits(in:)

Calculates and returns the most appropriate size for the current view.

macOS 10.15+

    
    
    @MainActor
    func sizeThatFits(in size: CGSize) -> CGSize

##  Parameters

`size`

    

The proposed new size for the view.

## Return Value

The size that offers the best fit for the root view and its contents.

## See Also

### Configuring the controller

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# preferredContentSize

macOS 10.15+

    
    
    @MainActor
    override dynamic var preferredContentSize: NSSize { get set }

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# sizingOptions

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

macOS 13.0+

    
    
    @MainActor
    var sizingOptions: NSHostingSizingOptions { get set }

## Discussion

NSHostingController can create minimum, maximum, and ideal (content size)
constraints that are derived from its SwiftUI view content. These constraints
are only created when Auto Layout constraints are otherwise being used in the
containing window.

If the NSHostingController is set as the `contentViewController` of an
`NSWindow`, it will also update the window’s `contentMinSize` and
`contentMaxSize` based on the minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`,
`intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to
control this behavior. For instance, setting a value of `.minSize` will only
create the constraints necessary to maintain the minimum size of the SwiftUI
content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingController`
relative to its displayed content, such as the always being displayed in a
fixed frame, setting this to a value with fewer options can improve
performance as it reduces the amount of layout measurements that need to be
performed. If an `NSHostingController` has a `frame` that is smaller or larger
than that required to display its SwiftUI content, the content will be
centered within that frame.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# safeAreaRegions

The safe area regions that this view controller adds to its view.

macOS 13.3+

    
    
    @MainActor
    var safeAreaRegions: SafeAreaRegions { get set }

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var sceneBridgingOptions: NSHostingSceneBridgingOptions`

The options for which aspects of the window will be managed by this
controller’s hosting view.

Instance Property

# sceneBridgingOptions

The options for which aspects of the window will be managed by this
controller’s hosting view.

macOS 14.0+

    
    
    @MainActor
    var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }

## Discussion

`NSHostingController` will populate certain aspects of its associated window,
depending on which options are specified.

For example, a hosting controller can manage its window’s toolbar by including
the `.toolbars` option:

When this hosting controller is set as the `contentViewController` for a
window, the default value for this property will be `.all`, which includes the
options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.

## See Also

### Configuring the controller

`func sizeThatFits(in: CGSize) -> CGSize`

Calculates and returns the most appropriate size for the current view.

`var preferredContentSize: NSSize`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting controller’s view creates and updates
constraints based on the size of its SwiftUI content.

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

