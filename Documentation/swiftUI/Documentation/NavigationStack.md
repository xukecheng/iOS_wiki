Initializer

# init(root:)

Creates a navigation stack that manages its own navigation state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(@ViewBuilder root: () -> Root) where Data == NavigationPath

##  Parameters

`root`

    

The view to display when the stack is empty.

## Discussion

If you want to access the navigation state, use `init(path:root:)` instead.

Initializer

# init(path:root:)

Creates a navigation stack with homogeneous navigation state that you can
control.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        path: Binding<Data>,
        @ViewBuilder root: () -> Root
    ) where Data : MutableCollection, Data : RandomAccessCollection, Data : RangeReplaceableCollection, Data.Element : Hashable

##  Parameters

`path`

    

A `Binding` to the navigation state for this stack.

`root`

    

The view to display when the stack is empty.

## Discussion

If you prefer to store the navigation state as a `NavigationPath`, use
`init(path:root:)` instead. If you don’t need access to the navigation state,
use `init(root:)`.

## See Also

### Creating a navigation stack with a path

`init(path: Binding<NavigationPath>, root: () -> Root)`

Creates a navigation stack with heterogeneous navigation state that you can
control.

Initializer

# init(path:root:)

Creates a navigation stack with heterogeneous navigation state that you can
control.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        path: Binding<NavigationPath>,
        @ViewBuilder root: () -> Root
    ) where Data == NavigationPath

##  Parameters

`path`

    

A `Binding` to the navigation state for this stack.

`root`

    

The view to display when the stack is empty.

## Discussion

If you prefer to store the navigation state as a collection of data values,
use `init(path:root:)` instead. If you don’t need access to the navigation
state, use `init(root:)`.

## See Also

### Creating a navigation stack with a path

`init(path: Binding<Data>, root: () -> Root)`

Creates a navigation stack with homogeneous navigation state that you can
control.

