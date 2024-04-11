Instance Method

# sizeThatFits(proposal:subviews:cache:)

Returns the size of the composite view, given a proposed size and the view’s
subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGSize

**Required**

##  Parameters

`proposal`

    

A size proposal for the container. The container’s parent view that calls this
method might call the method more than once with different proposals to learn
more about the container’s flexibility before deciding which proposal to use
for placement.

`subviews`

    

A collection of proxies that represent the views that the container arranges.
You can use the proxies in the collection to get information about the
subviews as you determine how much space the container needs to display them.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

A size that indicates how much space the container needs to arrange its
subviews.

## Discussion

Implement this method to tell your custom layout container’s parent view how
much space the container needs for a set of subviews, given a size proposal.
The parent might call this method more than once during a layout pass with
different proposed sizes to test the flexibility of the container, using
proposals like:

  * The `zero` proposal; respond with the layout’s minimum size.

  * The `infinity` proposal; respond with the layout’s maximum size.

  * The `unspecified` proposal; respond with the layout’s ideal size.

The parent might also choose to test flexibility in one dimension at a time.
For example, a horizontal stack might propose a fixed height and an infinite
width, and then the same height with a zero width.

The following example calculates the size for a basic vertical stack that
places views in a column, with no spacing between the views:

The implementation asks each subview for its ideal size by calling the
`sizeThatFits(_:)` method with an `unspecified` proposed size. It then reduces
these values into a single size that represents the maximum subview width and
the sum of subview heights. Because this example isn’t flexible, it ignores
its size proposal input and always returns the same value for a given set of
subviews.

SwiftUI views choose their own size, so the layout engine always uses a value
that you return from this method as the actual size of the composite view.
That size factors into the construction of the `bounds` input to the
`placeSubviews(in:proposal:subviews:cache:)` method.

## See Also

### Sizing the container and placing subviews

`func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

Instance Method

# placeSubviews(in:proposal:subviews:cache:)

Assigns positions to each of the layout’s subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    )

**Required**

##  Parameters

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space. Place all the container’s subviews
within the region. The size of this region matches a size that your container
previously returned from a call to the
`sizeThatFits(proposal:subviews:cache:)` method.

`proposal`

    

The size proposal from which the container generated the size that the parent
used to create the `bounds` parameter. The parent might propose more than one
size before calling the placement method, but it always uses one of the
proposals and the corresponding returned size when placing the container.

`subviews`

    

A collection of proxies that represent the views that the container arranges.
Use the proxies in the collection to get information about the subviews and to
tell the subviews where to appear.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Discussion

SwiftUI calls your implementation of this method to tell your custom layout
container to place its subviews. From this method, call the
`place(at:anchor:proposal:)` method on each element in `subviews` to tell the
subviews where to appear in the user interface.

For example, you can create a basic vertical stack that places views in a
column, with views horizontally aligned on their leading edge:

The example creates a placement point that starts at the origin of the
specified `bounds` input and uses that to place the first subview. It then
moves the point in the y dimension by the subview’s height, which it reads
using the `dimensions(in:)` method. This prepares the point for the next
iteration of the loop. All subview operations use an `unspecified` size
proposal to indicate that subviews should use and report their ideal size.

A more complex layout container might add space between subviews according to
their `spacing` preferences, or a fixed space based on input configuration.
For example, you can extend the basic vertical stack’s placement method to
calculate the preferred distances between adjacent subviews and store the
results in an array:

The spacing’s `distance(to:along:)` method considers the preferences of
adjacent views on the edge where they meet. It returns the smallest distance
that satisfies both views’ preferences for the given edge. For example, if one
view prefers at least `2` points on its bottom edge, and the next view prefers
at least `8` points on its top edge, the distance method returns `8`, because
that’s the smallest value that satisfies both preferences.

Update the placement calculations to use the spacing values:

Be sure that you use computations during placement that are consistent with
those in your implementation of other protocol methods for a given set of
inputs. For example, if you add spacing during placement, make sure your
implementation of `sizeThatFits(proposal:subviews:cache:)` accounts for the
extra space. Similarly, if the sizing method returns different values for
different size proposals, make sure the placement method responds to its
`proposal` input in the same way.

## See Also

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

Type Alias

# Layout.Subviews

A collection of proxies for the subviews of a layout view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Subviews = LayoutSubviews

## Discussion

This collection doesn’t store views. Instead it stores instances of
`LayoutSubview`, each of which acts as a proxy for one of the views arranged
by the layout. Use the proxies to get information about the views, and to tell
the views where to appear.

For more information about the behavior of the underlying collection type, see
`LayoutSubviews`.

## See Also

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

Instance Method

# explicitAlignment(of:in:proposal:subviews:cache:)

Returns the position of the specified horizontal alignment guide along the x
axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func explicitAlignment(
        of guide: HorizontalAlignment,
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGFloat?

**Required** Default implementations provided.

##  Parameters

`guide`

    

The `HorizontalAlignment` guide that the method calculates the position of.

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space.

`proposal`

    

A proposed size for the container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you determine where to place the guide.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

The guide’s position relative to the `bounds`. Return `nil` to indicate that
the guide doesn’t have an explicit value.

## Discussion

Implement this method to return a value for the specified alignment guide of a
custom layout container. The value you return affects the placement of the
container as a whole, but it doesn’t affect how the container arranges
subviews relative to one another.

You can use this method to put an alignment guide in a nonstandard position.
For example, you can indent the container’s leading edge alignment guide by 10
points:

The above example returns `nil` for other guides to indicate that they don’t
have an explicit value. A guide without an explicit value behaves as it would
for any other view. If you don’t implement the method, the protocol’s default
implementation merges the subviews’ guides.

## Default Implementations

### Layout Implementations

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the vertical alignment guides of all subviews.

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the horizontal alignment guides of all subviews.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Instance Method

# explicitAlignment(of:in:proposal:subviews:cache:)

Returns the position of the specified vertical alignment guide along the y
axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func explicitAlignment(
        of guide: VerticalAlignment,
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGFloat?

**Required** Default implementations provided.

##  Parameters

`guide`

    

The `VerticalAlignment` guide that the method calculates the position of.

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space.

`proposal`

    

A proposed size for the container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you determine where to place the guide.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

The guide’s position relative to the `bounds`. Return `nil` to indicate that
the guide doesn’t have an explicit value.

## Discussion

Implement this method to return a value for the specified alignment guide of a
custom layout container. The value you return affects the placement of the
container as a whole, but it doesn’t affect how the container arranges
subviews relative to one another.

You can use this method to put an alignment guide in a nonstandard position.
For example, you can raise the container’s bottom edge alignment guide by 10
points:

The above example returns `nil` for other guides to indicate that they don’t
have an explicit value. A guide without an explicit value behaves as it would
for any other view. If you don’t implement the method, the protocol’s default
implementation merges the subviews’ guides.

## Default Implementations

### Layout Implementations

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the vertical alignment guides of all subviews.

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the horizontal alignment guides of all subviews.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Instance Method

# spacing(subviews:cache:)

Returns the preferred spacing values of the composite view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func spacing(
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> ViewSpacing

**Required** Default implementation provided.

##  Parameters

`subviews`

    

A collection of proxy instances that represent the views that the container
arranges. You can use the proxies in the collection to get information about
the subviews as you determine how much spacing the container prefers around
it.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

A `ViewSpacing` instance that describes the preferred spacing around the
container view.

## Discussion

Implement this method to provide custom spacing preferences for a layout
container. The value you return affects the spacing around the container, but
it doesn’t affect how the container arranges subviews relative to one another
inside the container.

Create a custom `ViewSpacing` instance for your container by initializing one
with default values, and then merging that with spacing instances of certain
subviews. For example, if you define a basic vertical stack that places
subviews in a column, you could use the spacing preferences of the subview
edges that make contact with the container’s edges:

In the above example, the first and last subviews contribute to the spacing
above and below the container, respectively, while all subviews affect the
spacing on the leading and trailing edges.

If you don’t implement this method, the protocol provides a default
implementation, namely `spacing(subviews:cache:)`, that merges the spacing
preferences across all subviews on all edges.

## Default Implementations

### Layout Implementations

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the union of all subview spacing.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Type Property

# layoutProperties

Properties of a layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var layoutProperties: LayoutProperties { get }

**Required** Default implementation provided.

## Discussion

Implement this property in a type that conforms to the `Layout` protocol to
characterize your custom layout container. For example, you can indicate that
your layout has a vertical `stackOrientation`:

If you don’t implement this property in your custom layout, the protocol
provides a default implementation, namely `layoutProperties`, that returns a
`LayoutProperties` instance with default values.

## Default Implementations

### Layout Implementations

`static var layoutProperties: LayoutProperties`

The default property values for a layout.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

Instance Method

# makeCache(subviews:)

Creates and initializes a cache for a layout instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func makeCache(subviews: Self.Subviews) -> Self.Cache

**Required** Default implementation provided.

##  Parameters

`subviews`

    

A collection of proxy instances that represent the views that the container
arranges. You can use the proxies in the collection to get information about
the subviews as you calculate values to store in the cache.

## Return Value

Storage for calculated data that you share among the methods of your custom
layout container.

## Discussion

You can optionally use a cache to preserve calculated values across calls to a
layout container’s methods. Many layout types don’t need a cache, because
SwiftUI automatically reuses both the results of calls into the layout and the
values that the layout reads from its subviews. Rely on the protocol’s default
implementation of this method if you don’t need a cache.

However you might find a cache useful when:

  * The layout container repeats complex, intermediate calculations across calls like `sizeThatFits(proposal:subviews:cache:)`, `placeSubviews(in:proposal:subviews:cache:)`, and `explicitAlignment(of:in:proposal:subviews:cache:)`. You might be able to improve performance by calculating values once and storing them in a cache.

  * The layout container reads many `LayoutValueKey` values from subviews. It might be more efficient to do that once and store the results in the cache, rather than rereading the subviews’ values before each layout call.

  * You want to maintain working storage, like temporary Swift arrays, across calls into the layout, to minimize the number of allocation events.

Only implement a cache if profiling shows that it improves performance.

### Initialize a cache

Implement the `makeCache(subviews:)` method to create a cache. You can add
computed values to the cache right away, using information from the `subviews`
input parameter, or you can do that later. The methods of the `Layout`
protocol that can access the cache take the cache as an in-out parameter,
which enables you to modify the cache anywhere that you can read it.

You can use any storage type that makes sense for your layout algorithm, but
be sure that you only store data that you derive from the layout and its
subviews (lazily, if possible). For this to work correctly, SwiftUI needs to
be able to call this method to recreate the cache without changing the layout
result.

When you return a cache from this method, you implicitly define a type for
your cache. Be sure to either make the type of the `cache` parameters on your
other `Layout` protocol methods match, or use a type alias to define the
`Cache` associated type.

### Update the cache

If the layout container or any of its subviews change, SwiftUI calls the
`updateCache(_:subviews:)` method so you can modify or invalidate the contents
of the cache. The default implementation of that method calls the
`makeCache(subviews:)` method to recreate the cache, but you can provide your
own implementation of the update method to take an incremental approach, if
appropriate.

## Default Implementations

### Layout Implementations

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Returns the empty value when your layout doesn’t require a cache.

Available when `Cache` is `()`.

## See Also

### Managing a cache

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

Instance Method

# updateCache(_:subviews:)

Updates the layout’s cache when something changes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func updateCache(
        _ cache: inout Self.Cache,
        subviews: Self.Subviews
    )

**Required** Default implementation provided.

##  Parameters

`cache`

    

Storage for calculated data that you share among the methods of your custom
layout container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you calculate values to store in the cache.

## Discussion

If your custom layout container creates a cache by implementing the
`makeCache(subviews:)` method, SwiftUI calls the update method when your
layout or its subviews change, giving you an opportunity to modify or
invalidate the contents of the cache. The method’s default implementation
recreates the cache by calling the `makeCache(subviews:)` method, but you can
provide your own implementation to take an incremental approach, if
appropriate.

## Default Implementations

### Layout Implementations

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Reinitializes a cache to a new value.

## See Also

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

Associated Type

# Cache

Cached values associated with the layout instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Cache = Void

**Required**

## Discussion

If you create a cache for your custom layout, you can use a type alias to
define this type as your data storage type. Alternatively, you can refer to
the data storage type directly in all the places where you work with the
cache.

See `makeCache(subviews:)` for more information.

## See Also

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

Instance Method

# callAsFunction(_:)

Combines the specified views into a single composite view using the layout
algorithms of the custom layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func callAsFunction<V>(@ViewBuilder _ content: () -> V) -> some View where V : View
    

##  Parameters

`content`

    

A `ViewBuilder` that contains the views to lay out.

## Return Value

A composite view that combines all the input views.

## Discussion

Don’t call this method directly. SwiftUI calls it when you instantiate a
custom layout that conforms to the `Layout` protocol:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

