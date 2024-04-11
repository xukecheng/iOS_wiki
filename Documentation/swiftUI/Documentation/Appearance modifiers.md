Instance Method

# backgroundStyle(_:)

Sets the specified style to render backgrounds within the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

## Discussion

The following example uses this modifier to set the `backgroundStyle`
environment value to a `blue` color that includes a subtle `gradient`. SwiftUI
fills the `Circle` shape that acts as a background element with this style:

To restore the default background style, set the `backgroundStyle` environment
value to `nil` using the `environment(_:_:)` modifer:

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:)

Sets a view’s foreground elements to use a given style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The color or pattern to use when filling in the foreground elements. To
indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or one
of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`. To
set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

## Return Value

A view that uses the given foreground style.

## Discussion

Use this method to style foreground content like text, shapes, and template
images (including symbols):

The example above creates a row of `teal` foreground elements:

You can use any style that conforms to the `ShapeStyle` protocol, like the
`teal` color in the example above, or the
`linearGradient(colors:startPoint:endPoint:)` gradient shown below:

Tip

If you want to fill a single `Shape` instance with a style, use the
`fill(style:)` shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a
`Color` that you load from an asset catalog can have different light and dark
appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a
style of their own, but instead modify other styles. In particular, they
modify the primary level of the current foreground style to the degree given
by the hierarchical style’s name. To find the current foreground style to
modify, SwiftUI looks for the innermost containing style that you apply with
the `foregroundStyle(_:)` or the `foregroundColor(_:)` modifier. If you
haven’t specified a style, SwiftUI uses the default foreground style, as in
the following example:

If you add a foreground style on the enclosing `VStack`, the hierarchical
styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect
for foreground elements in that view, or in any of its child views, that it
would otherwise gain from adding a background material — for example, using
the `background(_:ignoresSafeAreaEdges:)` modifier. However, hierarchical
styles applied to the default foreground don’t disable vibrancy.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:)

Sets the primary and secondary levels of the foreground style in the child
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2>(
        _ primary: S1,
        _ secondary: S2
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:_:)

Sets the primary, secondary, and tertiary levels of the foreground style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2, S3>(
        _ primary: S1,
        _ secondary: S2,
        _ tertiary: S3
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

`tertiary`

    

The tertiary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# allowedDynamicRange(_:)

Returns a new view configured with the specified allowed dynamic range.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func allowedDynamicRange(_ range: Image.DynamicRange?) -> some View
    

##  Parameters

`range`

    

the requested dynamic range, or nil to restore the default allowed range.

## Return Value

a new view.

## Discussion

The following example enables HDR rendering within a view hierarchy:

## See Also

### Colors and patterns

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

Instance Method

# tint(_:)

Sets the tint within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tint<S>(_ tint: S?) -> some View where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

Use this method to override the default accent color for this view with a
given styling. Unlike an app’s accent color, which can be overridden by user
preference, tint is always respected and should be used as a way to provide
additional meaning to the control.

Controls which are unable to style themselves using the given type of
`ShapeStyle` will try to approximate the styling as best as they can (i.e.
controls which can not style themselves using a gradient will attempt to use
the color of the gradient’s first stop).

This example shows a linear dashboard styled gauge tinted with a gradient from
`green` to `red`.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint(Color?) -> some View`

Sets the tint color within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# tint(_:)

Sets the tint color within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func tint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The tint `Color` to apply.

## Discussion

Use this method to override the default accent color for this view. Unlike an
app’s accent color, which can be overridden by user preference, the tint color
is always respected and should be used as a way to provide additional meaning
to the control.

This example shows Answer and Decline buttons with `green` and `red` tint
colors, respectively.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# listRowSeparatorTint(_:edges:)

Sets the tint color associated with a row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the row separators, or `nil` to use the default color
for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose row separators are
tinted based on row-specific data:

To hide a row separators, use `listRowSeparator(_:edges:)`. To hide or change
the tint color for a section separator, use `listSectionSeparator(_:edges:)`
and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparatorTint(_:edges:)

Sets the tint color associated with a section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the section separators, or `nil` to use the default
color for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are
tinted based on section-specific data:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To hide a
section separator, use `listSectionSeparator(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listItemTint(_:)

Sets a fixed tint color for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The color to use to tint the content. Use `nil` to avoid overriding the
inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

Note

This modifier is equivalent to using the version of the modifier that takes a
`ListItemTint` value and specifying the `tint` color in the corresponding
`fixed(_:)` input.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets the tint effect for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: ListItemTint?) -> some View
    

##  Parameters

`tint`

    

The tint effect to use. Use `nil` to avoid overriding the inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# preferredColorScheme(_:)

Sets the preferred color scheme for this presentation.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme for this view.

## Return Value

A view that sets the color scheme.

## Discussion

Use one of the values in `ColorScheme` with this modifier to set a preferred
color scheme for the nearest enclosing presentation, like a popover, a sheet,
or a window. The value that you set overrides the user’s Dark Mode selection
for that presentation. In the example below, the `Toggle` controls an
`isDarkMode` state variable, which in turn controls the color scheme of the
sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this
case are a `List` and a `Toggle` — the value that you set propagates up
through the view hierarchy to the enclosing presentation, or until another
color scheme modifier higher in the hierarchy overrides it. The value you set
also flows down to all child views of the enclosing presentation.

A common use for this modifier is to create side-by-side previews of the same
view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read
the `colorScheme` environment value:

## See Also

### Detecting and requesting the light or dark appearance

`var colorScheme: ColorScheme`

The color scheme of this environment.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Instance Method

# preferredSurroundingsEffect(_:)

Applies an effect to passthrough video.

visionOS 1.0+

    
    
    func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some View
    

##  Parameters

`effect`

    

The effect that you want to apply.

## Return Value

A view that exhibits the specified preference.

## Discussion

Use this modifier to indicate a preference for the appearance of passthrough
video when displaying the modified view. For example, you can enhance the
immersiveness of a scene that uses the default `mixed` immersion style by
applying the `systemDark` preference to a view inside the scene:

When the system presents the `Orbit` view in the above code, it also dims
passthrough video. This helps to draw attention to the scene’s virtual content
while still enabling people to remain aware of their surroundings.

Note

This modifier expresses a preference, but the system might not be able to
honor it.

Use a value of `nil` to indicate that you have no preference. You typically do
this to counteract a preference expressed by a view lower in the view
hierarchy.

## See Also

### Configuring passthrough

`struct SurroundingsEffect`

Effects that the system can apply to passthrough video.

Instance Method

# border(_:width:)

Adds a border to this view with the specified style and width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func border<S>(
        _ content: S,
        width: CGFloat = 1
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

A value that conforms to the `ShapeStyle` protocol, like a `Color` or
`HierarchicalShapeStyle`, that SwiftUI uses to fill the border.

`width`

    

The thickness of the border. The default is 1 pixel.

## Return Value

A view that adds a border with the specified style and width to this view.

## Discussion

Use this modifier to draw a border of a specified width around the view’s
frame. By default, the border appears inside the bounds of this view. For
example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same
width before adding the border:

## See Also

### Styling content

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# overlay(alignment:content:)

Layers the views that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the foreground views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw in front of this
view, stacked in the order that you list them. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a foreground.

## Discussion

Use this modifier to place one or more views in front of another view. For
example, you can place a group of stars on a `RoundedRectangle`:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can place a star and a
`Circle` on a field of `blue`:

Both the overlay modifier and the implicit `ZStack` composed from the overlay
content — the circle and the star — use a default `center` alignment. The star
appears centered on the circle, and both appear as a composite view centered
in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack
rather than to the individual views in the closure. You can see this if you
add the `bottom` alignment:

The circle and the star move down as a unit to align the stack’s bottom edge
with the bottom edge of the square, while the star remains centered on the
circle:

To control the placement of individual items inside the `content` closure,
either use a different overlay modifier for each item, as the earlier example
of stars in the corners of a rectangle demonstrates, or add an explicit
`ZStack` inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the
circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the
modified view and the overlay content into a `ZStack`. This can produce a
simpler view hierarchy, but changes the layout priority that SwiftUI applies
to the views. Use the overlay modifier when you want the modified view to
dominate the layout.

If you want to specify a `ShapeStyle` like a `Color` or a `Material` as the
overlay, use `overlay(_:ignoresSafeAreaEdges:)` instead. To specify a `Shape`,
use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:ignoresSafeAreaEdges:)

Layers the specified style in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI layers in
front of the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the overlay.
The default value is `all`. Specify an empty set to respect safe area insets
on all edges.

## Return Value

A view with the specified style drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `ShapeStyle` protocol,
like a `Color`, `Material`, or `HierarchicalShapeStyle`, in front of a view.
For example, you can overlay the `ultraThinMaterial` over a `Circle`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
overlay fills the entirety of the circle’s frame (which happens to be wider
than the circle is tall):

SwiftUI also limits the style’s extent to the view’s container-relative shape.
You can see this effect if you constrain the `CoveredCircle` view with a
`containerShape(_:)` modifier:

The overlay takes on the specified container shape:

By default, the overlay ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the overlay rather than
a style, use `overlay(alignment:content:)` instead. If you want to specify a
`Shape`, use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:in:fillStyle:)

Layers a shape that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws in front of
the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol — like
a `Rectangle`, `Circle`, or `Capsule` — in front of a view. Specify a
`ShapeStyle` that’s used to fill the shape. For example, you can overlay the
outline of one rectangle in front of another:

The example above uses the `inset(by:)` method to slightly reduce the size of
the overlaid rectangle, and the `stroke(lineWidth:)` method to fill only the
shape’s outline. This creates an inset border:

This modifier is a convenience method for layering a shape over a view. To
handle the more general case of overlaying a `View` — or a stack of views —
with control over the position, use `overlay(alignment:content:)` instead. To
cover a view with a `ShapeStyle`, use `overlay(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(alignment:content:)

Layers the views that you specify behind this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw behind this view,
stacked in a cascading order from bottom to top. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a background.

## Discussion

Use this modifier to place one or more views behind another view. For example,
you can place a collection of stars beind a `Text` view:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places behind the text:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can layer a vertical bar
behind a circle, with both of those behind a horizontal bar:

Both the background modifier and the implicit `ZStack` composed from the
background content — the circle and the vertical bar — use a default `center`
alignment. The vertical bar appears centered behind the circle, and both
appear as a composite view centered behind the horizontal bar:

If you specify an alignment for the background, it applies to the implicit
stack rather than to the individual views in the closure. You can see this if
you add the `leading` alignment:

The vertical bar and the circle move as a unit to align the stack with the
leading edge of the horizontal bar, while the vertical bar remains centered on
the circle:

To control the placement of individual items inside the `content` closure,
either use a different background modifier for each item, as the earlier
example of stars under text demonstrates, or add an explicit `ZStack` inside
the content closure with its own alignment:

The stack alignment ensures that the circle’s leading edge aligns with the
vertical bar’s, while the background modifier aligns the composite view with
the horizontal bar:

You can achieve layering without a background modifier by putting both the
modified view and the background content into a `ZStack`. This produces a
simpler view hierarchy, but it changes the layout priority that SwiftUI
applies to the views. Use the background modifier when you want the modified
view to dominate the layout.

If you want to specify a `ShapeStyle` like a `HierarchicalShapeStyle` or a
`Material` as the background, use `background(_:ignoresSafeAreaEdges:)`
instead. To specify a `Shape` or `InsettableShape`, use
`background(_:in:fillStyle:)` or `background(_:in:fillStyle:)`, respectively.
To configure the background of a presentation, like a sheet, use
`presentationBackground(alignment:content:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:ignoresSafeAreaEdges:)

Sets the view’s background to a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI draws behind
the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the specified style drawn behind it.

## Discussion

Use this modifier to place a type that conforms to the `ShapeStyle` protocol —
like a `Color`, `Material`, or `HierarchicalShapeStyle` — behind a view. For
example, you can add the `regularMaterial` behind a `Label`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
background fills the entirety of the label’s frame, which includes the
padding:

SwiftUI limits the background style’s extent to the modified view’s container-
relative shape. You can see this effect if you constrain the `FlagLabel` view
with a `containerShape(_:)` modifier:

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(ignoresSafeAreaEdges:)

Sets the view’s background to the default background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the `background` shape style drawn behind it.

## Discussion

This modifier behaves like `background(_:ignoresSafeAreaEdges:)`, except that
it always uses the `background` shape style. For example, you can add a
background to a `Label`:

Without the background modifier, the teal color behind the label shows through
the label. With the modifier, the label’s text and icon appear backed by a
region filled with a color that’s appropriate for light or dark appearance:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to an insettable shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : InsettableShape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `InsettableShape`
protocol — like a `Rectangle`, `Circle`, or `Capsule` — behind a view. Specify
the `ShapeStyle` that’s used to fill the shape. For example, you can place a
`RoundedRectangle` behind a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to an insettable shape filled with the default
background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified insettable
shape. For example, you can use a `RoundedRectangle` as a background on a
`Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to a shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol behind
a view. Specify the `ShapeStyle` that’s used to fill the shape. For example,
you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to a shape filled with the default background
style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified shape. For
example, you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# alternatingRowBackgrounds(_:)

Overrides whether lists and tables in this view have alternating row
backgrounds.

macOS 14.0+

    
    
    func alternatingRowBackgrounds(_ behavior: AlternatingRowBackgroundBehavior = .enabled) -> some View
    

##  Parameters

`behavior`

    

Whether alternating row backgrounds are enabled or not.

## Discussion

This can be used in conjunction with an explicit list or table style or used
by itself to customize the row backgrounds of the automatic style. The only
list style this has no effect on is `.sidebar.`

This is able to be combined with `scrollContentBackground(_:)` and applies an
alternating row background on top of the overall list or table background.

This can also be combined with `listRowBackground`, which overrides the
background for a specific list row, replacing the automatic alternating
background for that row.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# listRowBackground(_:)

Places a custom background view behind a list row item.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowBackground<V>(_ view: V?) -> some View where V : View
    

##  Parameters

`view`

    

The `View` to use as the background behind the list row view.

## Return Value

A list row view with `view` as its background view.

## Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list
row item.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowBackground(_:)`
modifier then places the view you supply behind each of the list row items:

## See Also

### Configuring backgrounds

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# scrollContentBackground(_:)

Specifies the visibility of the background for scrollable views within this
view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func scrollContentBackground(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

the visibility to use for the background.

## Discussion

The following example hides the standard system background of the List.

## See Also

### Managing content visibility

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

Instance Method

# containerBackground(_:for:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<S>(
        _ style: S,
        for container: ContainerBackgroundPlacement
    ) -> some View where S : ShapeStyle
    

## Discussion

The following example uses a `LinearGradient` as a background:

The `.containerBackground(_:for:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

  * Parameters

    * style: The shape style to use as the container background.

    * container: The container that will use the background.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(for:alignment:content:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<V>(
        for container: ContainerBackgroundPlacement,
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`container`

    

The container that will use the background.

`content`

    

The view to use as the background of the container.

## Discussion

The following example uses a custom `View` as a background:

The `.containerBackground(for:alignment:content:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# glassBackgroundEffect(displayMode:)

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

visionOS 1.0+

    
    
    func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode = .always) -> some View
    

##  Parameters

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

## See Also

### Adding a glass background

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# glassBackgroundEffect(in:displayMode:)

Fills the view’s background with a glass material using a shape that you
specify.

visionOS 1.0+

    
    
    func glassBackgroundEffect<S>(
        in shape: S,
        displayMode: GlassBackgroundDisplayMode = .always
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An `InsettableShape` instance that SwiftUI draws behind the view. Unsupported
shapes resolve to a rectangle.

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

Prefer a shape for the background that has rounded corners. An unsupported
shape style resolves to a rectangle.

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# defaultWheelPickerItemHeight(_:)

Sets the default wheel-style picker item height.

watchOS 6.0+  visionOS 1.0+

    
    
    func defaultWheelPickerItemHeight(_ height: CGFloat) -> some View
    

##  Parameters

`height`

    

The height for the picker items.

## Discussion

Use `defaultWheelPickerItemHeight(_:)` when you need to change the default
item height in a picker control. In this example, the view sets the default
height for picker elements to 30 points.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# horizontalRadioGroupLayout()

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

macOS 10.15+

    
    
    func horizontalRadioGroupLayout() -> some View
    

## Discussion

Use `horizontalRadioGroupLayout()` to configure the visual layout of radio
buttons in a `Picker` so that the radio buttons are arranged horizontally in
the view.

The example below shows two `Picker` controls configured as radio button
groups; the first group shows the default vertical layout; the second group
shows the effect of `horizontalRadioGroupLayout()` which renders the radio
buttons horizontally.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# controlSize(_:)

Sets the size for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func controlSize(_ controlSize: ControlSize) -> some View
    

##  Parameters

`controlSize`

    

One of the control sizes specified in the `ControlSize` enumeration.

## Discussion

Use `controlSize(_:)` to override the system default size for controls in this
view. In this example, a view displays several typical controls at `.mini`,
`.small` and `.regular` sizes.

## See Also

### Sizing controls

`var controlSize: ControlSize`

The size to apply to controls within a view.

`enum ControlSize`

The size classes, like regular or small, that you can apply to controls within
a view.

Instance Method

# buttonBorderShape(_:)

Sets the border shape for buttons in this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func buttonBorderShape(_ shape: ButtonBorderShape) -> some View
    

##  Parameters

`shape`

    

the shape to use.

## Discussion

The border shape is used to draw the platter for a bordered button. On macOS,
the specified border shape is only applied to bordered buttons in widgets.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonRepeatBehavior(_:)

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View
    

##  Parameters

`behavior`

    

A value of `enabled` means that buttons should enable repeating behavior and a
value of `disabled` means that buttons should disallow repeating behavior.

## Discussion

Apply this to buttons that increment or decrement a value or perform some
other inherently iterative operation. Interactions such as pressing-and-
holding on the button, holding the button’s keyboard shortcut, or holding down
the space key while the button is focused will trigger this repeat behavior.

This affects all system button styles, as well as automatically affects custom
`ButtonStyle` conforming types. This does not automatically apply to custom
`PrimitiveButtonStyle` conforming types, and the
`EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their
custom gestures as appropriate.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# headerProminence(_:)

Sets the header prominence for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func headerProminence(_ prominence: Prominence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply.

## Discussion

In the following example, the section header appears with increased
prominence:

## See Also

### Configuring headers

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Method

# scrollDisabled(_:)

Disables or enables scrolling in scrollable views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollDisabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean that indicates whether scrolling is disabled.

## Discussion

Use this modifier to control whether a `ScrollView` can scroll:

SwiftUI passes the disabled property through the environment, which means you
can use this modifier to disable scrolling for all scroll views within a view
hierarchy. In the following example, the modifier affects both scroll views:

You can also use this modifier to disable scrolling for other kinds of
scrollable views, like a `List` or a `TextEditor`.

## See Also

### Disabling scrolling

`var isScrollEnabled: Bool`

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

Instance Method

# scrollBounceBehavior(_:axes:)

Configures the bounce behavior of scrollable views along the specified axis.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func scrollBounceBehavior(
        _ behavior: ScrollBounceBehavior,
        axes: Axis.Set = [.vertical]
    ) -> some View
    

##  Parameters

`behavior`

    

The bounce behavior to apply to any scrollable views within the configured
view. Use one of the `ScrollBounceBehavior` values.

`axes`

    

The set of axes to apply `behavior` to. The default is `Axis.vertical`.

## Return Value

A view that’s configured with the specified scroll bounce behavior.

## Discussion

Use this modifier to indicate whether scrollable views bounce when people
scroll to the end of the view’s content, taking into account the relative
sizes of the view and its content. For example, the following `ScrollView`
only enables bounce behavior if its content is large enough to require
scrolling:

The modifier passes the scroll bounce mode through the `Environment`, which
means that the mode affects any scrollable views in the modified view
hierarchy. Provide an axis to the modifier to constrain the kinds of
scrollable views that the mode affects. For example, all the scroll views in
the following example can access the mode value, but only the two nested
scroll views are affected, because only they use horizontal scrolling:

You can use this modifier to configure any kind of scrollable view, including
`ScrollView`, `List`, `Table`, and `TextEditor`:

## See Also

### Configuring scroll bounce behavior

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Method

# scrollIndicatorsFlash(onAppear:)

Flashes the scroll indicators of a scrollable view when it appears.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(onAppear: Bool) -> some View
    

##  Parameters

`onAppear`

    

A Boolean value that indicates whether the scroll indicators flash when the
scroll view appears.

## Return Value

A view that flashes any visible scroll indicators when it first appears.

## Discussion

Use this modifier to control whether the scroll indicators of a scroll view
briefly flash when the view first appears. For example, you can make the
indicators flash by setting the `onAppear` parameter to `true`:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a value changes, use `scrollIndicatorsFlash(trigger:)`
instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollIndicatorsFlash(trigger:)

Flashes the scroll indicators of scrollable views when a value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(trigger value: some Equatable) -> some View
    

##  Parameters

`value`

    

The value that causes scroll indicators to flash. The value must conform to
the `Equatable` protocol.

## Return Value

A view that flashes any visible scroll indicators when a value changes.

## Discussion

When the value that you provide to this modifier changes, the scroll
indicators of any scrollable views within the modified view hierarchy briefly
flash. The following example configures the scroll indicators to flash any
time `flashCount` changes:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a scroll view initially appears, use
`scrollIndicatorsFlash(onAppear:)` instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# menuOrder(_:)

Sets the preferred order of items for menus presented from this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func menuOrder(_ order: MenuOrder) -> some View
    

##  Parameters

`order`

    

The menu item ordering strategy to apply.

## Return Value

A view that uses the specified menu ordering strategy.

## Discussion

Use this modifier to override the default menu order. On supported platforms,
`priority` order keeps the first items closer to the user’s point of
interaction, whereas `fixed` order always orders items from top to bottom.

On iOS, the `automatic` order resolves to `fixed` for menus presented within
scrollable content. Pickers that use the `menu` style also default to `fixed`
order. In all other cases, menus default to `priority` order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to `fixed`
order.

The following example creates a menu that presents its content in a fixed
order from top to bottom:

You can use this modifier on controls that present a menu. For example, the
code below creates a `Picker` using the `menu` style with a priority-based
order:

You can also use this modifier on context menus. The example below creates a
context menu that presents its content in a fixed order:

The modifier has no effect when applied to a subsection or submenu of a menu.

## See Also

### Setting a preferred order

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

`struct MenuOrder`

The order in which a menu presents its content.

Instance Method

# menuActionDismissBehavior(_:)

Tells a menu whether to dismiss after performing an action.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func menuActionDismissBehavior(_ behavior: MenuActionDismissBehavior) -> some View
    

##  Parameters

`dismissal`

    

The menu action dismissal behavior to apply.

## Return Value

A view that has the specified menu dismissal behavior.

## Discussion

Use this modifier to control the dismissal behavior of a menu. In the example
below, the menu doesn’t dismiss after someone chooses either the increase or
decrease action:

You can use this modifier on any controls that present a menu, like a `Picker`
that uses the `menu` style or a `ControlGroup`. For example, the code below
creates a picker that disables dismissal when someone selects one of the
options:

You can also use this modifier on context menus. The example below creates a
context menu that stays presented after someone selects an action to run:

## See Also

### Configuring menu dismissal

`struct MenuActionDismissBehavior`

The set of menu dismissal behavior options.

Instance Method

# paletteSelectionEffect(_:)

Specifies the selection effect to apply to a palette item.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func paletteSelectionEffect(_ effect: PaletteSelectionEffect) -> some View
    

##  Parameters

`effect`

    

The type of effect to apply when a palette item is selected.

## Discussion

`automatic` applies the system’s default appearance when selected. When using
un-tinted SF Symbols or template images, the current tint color is applied to
the selected items’ image. If the provided SF Symbols have custom tints, a
stroke is drawn around selected items.

If you wish to provide a specific image (or SF Symbol) to indicate selection,
use `custom` to forgo the system’s default selection appearance allowing the
provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system
selection behavior:

If a specific SF Symbol variant is preferable instead, use
`symbolVariant(_:)`.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ text: Text?) -> some View
    

##  Parameters

`text`

    

The explicit text value to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ stringKey: LocalizedStringKey) -> some View
    

##  Parameters

`stringKey`

    

The localized string key to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent<S>(_ string: S) -> some View where S : StringProtocol
    

##  Parameters

`string`

    

The string to use as a type select equivalent for a view in a collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# symbolEffect(_:options:isActive:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        isActive: Bool = true
    ) -> some View where T : IndefiniteSymbolEffect, T : SymbolEffect
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`isActive`

    

whether the effect is active or inactive.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a repeating pulse effect to two symbol images:

## See Also

### Managing symbol effects

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffect(_:options:value:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T, U>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        value: U
    ) -> some View where T : DiscreteSymbolEffect, T : SymbolEffect, U : Equatable
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`value`

    

the value to monitor for changes, the animation is triggered each time the
value changes.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a bounce effect to two symbol images, the animation
will play each time `counter` changes:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffectsRemoved(_:)

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffectsRemoved(_ isEnabled: Bool = true) -> some View
    

##  Parameters

`isEnabled`

    

Whether to remove inherited symbol effects or not.

## Return Value

a copy of the view with its symbol effects either removed or left unchanged.

## Discussion

The following example adds a repeating pulse effect to two symbol images, but
then disables the effect on one of them:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# privacySensitive(_:)

Marks the view as containing sensitive, private user data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func privacySensitive(_ sensitive: Bool = true) -> some View
    

## Discussion

SwiftUI redacts views marked with this modifier when you apply the `privacy`
redaction reason.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# redacted(reason:)

Adds a reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func redacted(reason: RedactionReasons) -> some View
    

## Discussion

Adding a redaction is an additive process: any redaction provided will be
added to the reasons provided by the parent.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# unredacted()

Removes any reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func unredacted() -> some View
    

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# invalidatableContent(_:)

Mark the receiver as their content might be invalidated.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func invalidatableContent(_ invalidatable: Bool = true) -> some View
    

##  Parameters

`invalidatable`

    

Whether the receiver content might be invalidated.

## Discussion

Use this modifier to annotate views that display values that are derived from
the current state of your data and might be invalidated in response of, for
example, user interaction.

The view will change its appearance when `RedactionReasons.invalidated` is
present in the environment.

In an interactive widget a view is invalidated from the moment the user
interacts with a control on the widget to the moment when a new timeline
update has been presented.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

Instance Method

# hidden()

Hides this view unconditionally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hidden() -> some View
    

## Return Value

A hidden view.

## Discussion

Hidden views are invisible and can’t receive or respond to interactions.
However, they do remain in the view hierarchy and affect layout. Use this
modifier if you want to include a view for layout purposes, but don’t want it
to display.

The third circle takes up space, because it’s still present, but SwiftUI
doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if`
statement instead:

Depending on the current value of the `isHidden` state variable in the example
above, controlled by the `Toggle` instance, SwiftUI draws the circle or
completely omits it from the layout.

## See Also

### Hiding views

`func opacity(Double) -> some View`

Sets the transparency of this view.

Instance Method

# labelsHidden()

Hides the labels of any controls contained within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func labelsHidden() -> some View
    

## Discussion

Use this modifier when you want to omit a label from one or more controls in
your user interface. For example, the first `Toggle` in the following example
hides its label:

The `VStack` in the example above centers the first toggle’s control element
in the available space, while it centers the second toggle’s combined label
and control element:

Always provide a label for controls, even when you hide the label, because
SwiftUI uses labels for other purposes, including accessibility.

Note

This modifier doesn’t work for all labels. It applies to labels that are
separate from the rest of the control’s interface, like they are for `Toggle`,
but not to controls like a bordered button where the label is inside the
button’s border.

## See Also

### Hiding system elements

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# menuIndicator(_:)

Sets the menu indicator visibility for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for
controls in this view. For example, the code below creates a menu without an
indicator:

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

Instance Method

# listRowSeparator(_:edges:)

Sets the display mode for the separator associated with this specific row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this row’s separators.

`edges`

    

The set of row edges for which this preference applies. The list style might
already decide to not display separators for some edges, typically the top
edge. The default is `all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are
hidden:

To change the color of a row separators, use `listRowSeparatorTint(_:edges:)`.
To hide or change the tint color for a section separators, use
`listSectionSeparator(_:edges:)` and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparator(_:edges:)

Sets whether to hide the separator associated with a list section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this section’s separators.

`edges`

    

The set of row edges for which the preference applies. The list style might
already decide to not display separators for some edges. The default is `all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections
separator are hidden:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To set the
tint color for a section separator, use `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

Instance Method

# persistentSystemOverlays(_:)

Sets the preferred visibility of the non-transient system views overlaying the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func persistentSystemOverlays(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value that indicates the visibility of the non-transient system views
overlaying the app.

## Discussion

Use this modifier if you would like to customise the immersive experience of
your app by hiding or showing system overlays that may affect user experience.
The following example hides every persistent system overlay.

Note that this modifier only sets a preference and, ultimately the system will
decide if it will honour it or not.

These non-transient system views include:

  * The Home indicator

  * The SharePlay indicator

  * The Multi-task indicator and Picture-in-picture on iPad

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# scrollIndicators(_:axes:)

Sets the visibility of scroll indicators within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollIndicators(
        _ visibility: ScrollIndicatorVisibility,
        axes: Axis.Set = [.vertical, .horizontal]
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility to apply to scrollable views.

`axes`

    

The axes of scrollable views that the visibility applies to.

## Return Value

A view with the specified scroll indicator visibility.

## Discussion

Use this modifier to hide or show scroll indicators on scrollable content in
views like a `ScrollView`, `List`, or `TextEditor`. This modifier applies the
prefered visibility to any scrollable content within a view hierarchy.

Use the `hidden` value to indicate that you prefer that views never show
scroll indicators along a given axis. Use `visible` when you prefer that views
show scroll indicators. Depending on platform conventions, visible scroll
indicators might only appear while scrolling. Pass `automatic` to allow views
to decide whether or not to show their indicators.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollClipDisabled(_:)

Sets whether a scroll view clips its content to its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollClipDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that specifies whether to disable scroll view clipping.

## Return Value

A view that disables or enables scroll view clipping.

## Discussion

By default, a scroll view clips its content to its bounds, but you can disable
that behavior by using this modifier. For example, if the views inside the
scroll view have shadows that extend beyond the bounds of the scroll view, you
can use this modifier to avoid clipping the shadows:

The scroll view in the above example clips when the content view’s `disabled`
input is `false`, as it does if you omit the modifier, but not when the input
is `true`:

  * True 
  * False 

While you might want to avoid clipping parts of views that exceed the bounds
of the scroll view, like the shadows in the above example, you typically still
want the scroll view to clip at some point. Create custom clipping by using
the `clipShape(_:style:)` modifier to add a different clip shape. The
following code disables the default clipping and then adds rectangular
clipping that exceeds the bounds of the scroll view by the default padding
amount:

## See Also

### Managing content visibility

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

Instance Method

# tableColumnHeaders(_:)

Controls the visibility of a `Table`’s column header views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func tableColumnHeaders(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value of `visible` will show table columns, `hidden` will remove them, and
`automatic` will defer to default behavior.

## Discussion

By default, `Table` will display a global header view with the labels of each
table column. This area is also where users can sort, resize, and rearrange
the columns. For simple cases that don’t require those features, this header
can be hidden.

This will not affect the header of any `Section`s in a table.

## See Also

### Customizing columns

`struct TableColumnCustomization`

A representation of the state of the columns in a table.

`struct TableColumnCustomizationBehavior`

A set of customization behaviors of a column that a table can offer to a user.

Instance Method

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some View
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some Scene`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# sensoryFeedback(_:trigger:)

Plays the specified `feedback` when the provided `trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

## Discussion

For example, you could play feedback when a state value changes:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(trigger:_:)

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        trigger: T,
        _ feedback: @escaping (T, T) -> SensoryFeedback?
    ) -> some View where T : Equatable
    

##  Parameters

`trigger`

    

A value to monitor for changes to determine when to play.

`feedback`

    

A closure to determine whether to play the feedback and what type of feedback
to play when `trigger` changes.

## Discussion

For example, you could play different feedback for different state
transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(_:trigger:condition:)

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T,
        condition: @escaping (T, T) -> Bool
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

`condition`

    

A closure to determine whether to play the feedback when `trigger` changes.

## Discussion

For example, you could play feedback for certain state transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# widgetAccentable(_:)

Adds the view and all of its subviews to the accented group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetAccentable(_ accentable: Bool = true) -> some View
    

##  Parameters

`accentable`

    

A Boolean value that indicates whether to add the view and its subviews to the
accented group.

## Discussion

When the system renders the widget using the
`WidgetKit/WidgetRenderingMode/accented` mode, it divides the widget’s view
hierarchy into two groups: the accented group and the default group. It then
applies a different color to each group.

When applying the colors, the system treats the widget’s views as if they were
template images. It ignores the view’s color — rendering the new colors based
on the view’s alpha channel.

To control your view’s appearance, add the `widgetAccentable(_:)` modifier to
part of your view’s hierarchy. If the `accentable` parameter is `true`, the
system adds that view and all of its subviews to the accent group. It puts all
other views in the default group.

Important

After you call `widgetAccentable(true)` on a view moving it into the accented
group, calling `widgetAccentable(false)` on its subviews doesn’t move the
subviews back into the default group.

Instance Method

# widgetCurvesContent(_:)

Displays the widget’s content along a curve if the context allows it.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func widgetCurvesContent(_ curvesContent: Bool = true) -> some View
    

##  Parameters

`curvesContent`

    

A Boolean value that indicates whether the system curves the widget label’s
content, if the context allows.

## Discussion

The system positions the widget’s content along a curve that follows the
corner of the watch face when displaying a `WidgetFamily/accessoryCorner`
complication. The widget must use a `widgetLabel(_:)` modifier, and the
curving effect modifies only text, SF Symbols, and images.

When displaying an `.accessoryCorner` complication, the system places the
widget label on the inside of the curve, and the widget’s content on the
outside, as shown below.

The system can also curve text, SF symbols, and image content from a
`ViewThatFits` view.

## See Also

### Widget configuration

`func widgetAccentable(Bool) -> some View`

Adds the view and all of its subviews to the accented group.

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

`func dynamicIsland(verticalPlacement:
DynamicIslandExpandedRegionVerticalPlacement) -> some View`

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

Instance Method

# widgetLabel(_:)

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

A string that contains the text which WidgetKit displays alongside the
complication.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style. For
example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(_:)

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

A label generated from a localized string.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style based
on the clock face. For example, setting the font and rendering the text along
a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(label:)

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<Label>(@ViewBuilder label: () -> Label) -> some View where Label : View
    

##  Parameters

`label`

    

A view that WidgetKit can display alongside the accessory family widget’s main
SwiftUI view. You can use a `Image`, `Text`, `Gauge`, `ProgressView`, or a
container with multiple subviews.

## Discussion

The system only displays labels on widget-based complications in watchOS. The
system ignores any labels attached to widgets on the Lock Screen on iPhone.
Therefore, you can use the same code to display an accessory family widget on
both iPhone and Apple Watch.

To create the widget label, call `widgetLabel(label:)`on a complication’s main
SwiftUI view. Pass the desired content as the `label` parameter. The label can
be a `Gauge`, `ProgressView`, `Text`, or `Image`. To provide multiple views,
wrap your views in a container, such as a `VStack`. WidgetKit determines
whether it can use any of the label’s content. If it can’t, it ignores the
label.

WidgetKit configures the label so that the watch face presents a unified look.
For example, it sets the size for an image, the font for text, and can even
render text and gauges along a curve.

The following widget families support widget labels:

`WidgetKit/WidgetFamily/accessoryCorner`

    

In watchOS, this widget-based complication can display a `Gauge`, a
`ProgressView`, or a `Text`. Adding a label to an accessory corner causes the
main SwiftUI view to shrink to make space for the label. If you pass a view
containing multiple, valid subviews, the system picks which view to display as
the widget label.

`WidgetKit/WidgetFamily/accessoryCircular`

    

In watchOS, the widget-based complication can display either an `Image` or a
`Text`. To pass both an image and text, wrap those views in a container.

However, WidgetKit only renders the label along the bezel on the Infograph
watch face (the top circular complication). On all other circular
complications — including widgets on all other platforms — WidgetKit ignores
the label.

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

Instance Method

# dynamicIsland(verticalPlacement:)

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
    

##  Parameters

`verticalPlacement`

    

The vertical placement for a view that’s part of an expanded Live Activity in
the Dynamic Island.

## Return Value

A view with the specified vertical placement.

