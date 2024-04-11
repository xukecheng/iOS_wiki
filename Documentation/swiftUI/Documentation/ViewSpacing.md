Initializer

# init()

Initializes an instance with default spacing values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use this initializer to create a spacing preferences instance with default
values. Then use `formUnion(_:edges:)` to combine preferences from other views
with the new instance. You typically do this in a custom layout’s
implementation of the `spacing(subviews:cache:)` method.

## See Also

### Creating spacing instances

`static let zero: ViewSpacing`

A view spacing instance that contains zero on all edges.

Type Property

# zero

A view spacing instance that contains zero on all edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let zero: ViewSpacing

## Discussion

You typically only use this value for an empty view.

## See Also

### Creating spacing instances

`init()`

Initializes an instance with default spacing values.

Instance Method

# distance(to:along:)

Gets the preferred spacing distance along the specified axis to the view that
returns a specified spacing preference.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func distance(
        to next: ViewSpacing,
        along axis: Axis
    ) -> CGFloat

##  Parameters

`next`

    

The spacing preferences instance of the adjacent view.

`axis`

    

The axis that the two views align on.

## Return Value

A floating point value that represents the smallest distance in points between
two views that satisfies the spacing preferences of both this view and the
adjacent views on their shared edge.

## Discussion

Call this method from your implementation of `Layout` protocol methods if you
need to measure the default spacing between two views in a custom layout. Call
the method on the first view’s preferences instance, and provide the second
view’s preferences instance as input.

For example, consider two views that appear in a custom horizontal stack. The
following distance call gets the preferred spacing between these views, where
`spacing1` contains the preferences of a first view, and `spacing2` contains
the preferences of a second view:

The method first determines, based on the axis and the ordering, that the
views abut on the trailing edge of the first view and the leading edge of the
second. It then gets the spacing preferences for the corresponding edges of
each view, and returns the greater of the two values. This results in the
smallest value that provides enough space to satisfy the preferences of both
views.

Note

This method returns the default spacing between views, but a layout can choose
to ignore the value and use custom spacing instead.

Instance Method

# formUnion(_:edges:)

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func formUnion(
        _ other: ViewSpacing,
        edges: Edge.Set = .all
    )

##  Parameters

`other`

    

Another spacing preferences instances to merge with this one.

`edges`

    

The edges to merge. Edges that you don’t specify are unchanged after the
method completes.

## Discussion

When you merge another spacing preference instance with this one, this
instance ends up with the greater of its original value or the other
instance’s value for each of the specified edges. You can call the method
repeatedly with each value in a collection to merge a collection of
preferences. The result has the smallest preferences on each edge that meets
the largest requirements of all the inputs for that edge.

If you want to merge preferences without modifying the original instance, use
`union(_:edges:)` instead.

## See Also

### Merging spacing instances

`func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing`

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

Instance Method

# union(_:edges:)

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func union(
        _ other: ViewSpacing,
        edges: Edge.Set = .all
    ) -> ViewSpacing

##  Parameters

`other`

    

Another spacing preferences instance to merge with this one.

`edges`

    

The edges to merge. Edges that you don’t specify are unchanged after the
method completes.

## Return Value

A new view spacing preferences instance with the merged values.

## Discussion

This method behaves like `formUnion(_:edges:)`, except that it creates a copy
of the original spacing preferences instance before merging, leaving the
original instance unmodified.

## See Also

### Merging spacing instances

`func formUnion(ViewSpacing, edges: Edge.Set)`

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.

