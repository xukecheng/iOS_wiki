Initializer

# init(_:)

Creates a localized string key from the given string value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ value: String)

##  Parameters

`value`

    

The string to use as a localization key.

## See Also

### Creating a key from a literal value

`init(stringLiteral: String)`

Creates a localized string key from the given string literal.

Initializer

# init(stringLiteral:)

Creates a localized string key from the given string literal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(stringLiteral value: String)

##  Parameters

`value`

    

The string literal to use as a localization key.

## See Also

### Creating a key from a literal value

`init(String)`

Creates a localized string key from the given string value.

Initializer

# init(stringInterpolation:)

Creates a localized string key from the given string interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(stringInterpolation: LocalizedStringKey.StringInterpolation)

##  Parameters

`stringInterpolation`

    

The string interpolation to use as the localization key.

## Discussion

To create a localized string key from a string interpolation, use the `\()`
string interpolation syntax. Swift matches the parameter types in the
expression to one of the `appendInterpolation` methods in
`LocalizedStringKey.StringInterpolation`. The interpolated types can include
numeric values, Foundation types, and SwiftUI `Text` and `Image` instances.

The following example uses a string interpolation with two arguments: an
unlabeled `Date` and a `Text.DateStyle` labeled `style`. The compiler maps
these to the method `appendInterpolation(_:style:)` as it builds the string
that it creates the `LocalizedStringKey` with.

You can write this example more concisely, implicitly creating a
`LocalizedStringKey` as the parameter to the `Text` initializer:

## See Also

### Creating a key from an interpolation

`struct StringInterpolation`

Represents the contents of a string literal with interpolations while it’s
being built, for use in creating a localized string key.

Structure

# LocalizedStringKey.StringInterpolation

Represents the contents of a string literal with interpolations while it’s
being built, for use in creating a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct StringInterpolation

## Topics

### Appending to an interpolation

The compiler uses these methods when interpreting string interpolations; don’t
call them directly.

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

## Relationships

### Conforms To

  * `StringInterpolationProtocol`

## See Also

### Creating a key from an interpolation

`init(stringInterpolation: LocalizedStringKey.StringInterpolation)`

Creates a localized string key from the given string interpolation.

