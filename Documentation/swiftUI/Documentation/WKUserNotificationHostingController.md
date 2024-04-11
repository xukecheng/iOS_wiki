Initializer

# init()

Creates a notification hosting controller object that you can use to implement
your notification interfaces using SwiftUI views.

watchOS 6.0+

    
    
    @MainActor
    override dynamic init()

Instance Property

# body

The root view of the view hierarchy to display for your notification
interface.

watchOS 6.0+

    
    
    @MainActor
    var body: Body { get }

## Discussion

Override this property and return the root view of your SwiftUI view hierarchy
from your implementation. If you don’t override this property, accessing the
default implementation triggers an exception.

Type Property

# coalescedDescriptionFormat

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

watchOS 7.0+

    
    
    @MainActor
    class var coalescedDescriptionFormat: String? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# isInteractive

If the notification should accept user input.

watchOS 7.0+

    
    
    @MainActor
    class var isInteractive: Bool { get }

## Discussion

Default value is `false`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# sashColor

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var sashColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# subtitleColor

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var subtitleColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# titleColor

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

watchOS 7.0+

    
    
    @MainActor
    class var titleColor: Color? { get }

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var wantsSashBlur: Bool`

If the sash should include a blur over the background.

Type Property

# wantsSashBlur

If the sash should include a blur over the background.

watchOS 7.0+

    
    
    @MainActor
    class var wantsSashBlur: Bool { get }

## Discussion

Default value is `false`

## See Also

### Configuring the notification

`class var coalescedDescriptionFormat: String?`

The format string to display when multiple notifications of the same type
arrive simultaneously. If you specify a custom string, you can use the %d
variable to reflect the number of notifications. If `nil` format will be the
system default.

`class var isInteractive: Bool`

If the notification should accept user input.

`class var sashColor: Color?`

Color to use within the sash of the long look interface. If `nil` the sash
will be the default system color.

`class var subtitleColor: Color?`

The color to apply to the subtitle text displayed in the short look interface.
If `nil` the text will be the default system color.

`class var titleColor: Color?`

The color to apply to the text displayed in the sash. If `nil` the text will
be the default system color.

