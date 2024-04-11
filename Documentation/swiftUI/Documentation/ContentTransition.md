Type Property

# identity

The identity content transition, which indicates that content changes
shouldn’t animate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let identity: ContentTransition

## Discussion

You can pass this value to a `contentTransition(_:)` modifier to selectively
disable animations that would otherwise be applied by a `withAnimation(_:_:)`
block.

## See Also

### Getting content transitions

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# interpolate

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let interpolate: ContentTransition

## Discussion

Text views can interpolate transitions when the text views have identical
strings. Matching glyph pairs can animate changes to their color, position,
size, and any variable properties. Interpolation can apply within a
`Font.Design` case, but not between cases, or between entirely different
fonts. For example, you can interpolate a change between `thin` and `black`
variations of a font, since these are both cases of `Font.Weight`. However,
you can’t interpolate between the default design of a font and its Italic
version, because these are different fonts. Any changes that can’t show an
interpolated animation use an opacity animation instead.

Symbol images created with the `init(systemName:)` initializer work the same
way as text: changes within the same symbol attempt to interpolate the
symbol’s paths. When interpolation is unavailable, the system uses an opacity
transition instead.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# numericText(countsDown:)

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func numericText(countsDown: Bool = false) -> ContentTransition

##  Parameters

`countsDown`

    

true if the numbers represented by the text are counting downwards.

## Return Value

a new content transition.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# numericText(value:)

Creates a content transition intended to be used with `Text` views displaying
numbers.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func numericText(value: Double) -> ContentTransition

##  Parameters

`value`

    

the value represented by the `Text` view being animated. The difference
between the old and new values when the text changes will be used to determine
the animation direction.

## Return Value

a new content transition.

## Discussion

The example below creates a text view displaying a particular value, assigning
the same value to the associated transition:

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# opacity

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let opacity: ContentTransition

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# symbolEffect

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var symbolEffect: ContentTransition { get }

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# symbolEffect(_:options:)

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default
    ) -> ContentTransition where T : ContentTransitionSymbolEffect, T : SymbolEffect

##  Parameters

`config`

    

the animation configuration value.

## Return Value

a new content transition.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

