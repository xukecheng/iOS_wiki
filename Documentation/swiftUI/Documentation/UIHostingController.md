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

