Initializer

# init(_:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(_ title: S) where S : StringProtocol

Available when `Image` is `Never` and `Icon` is `Never`.

##  Parameters

`title`

    

A title to show in a preview.

## See Also

### Displaying a preview

`init(LocalizedStringKey)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

`init(Text)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

Initializer

# init(_:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(_ titleKey: LocalizedStringKey)

Available when `Image` is `Never` and `Icon` is `Never`.

##  Parameters

`titleKey`

    

A key identifying a title to show in a preview.

## See Also

### Displaying a preview

`init<S>(S)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

`init(Text)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

Initializer

# init(_:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(_ title: Text)

Available when `Image` is `Never` and `Icon` is `Never`.

##  Parameters

`title`

    

A title to show in a preview.

## See Also

### Displaying a preview

`init<S>(S)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

`init(LocalizedStringKey)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

Initializer

# init(_:image:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: Image
    ) where S : StringProtocol

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

##  Parameters

`title`

    

A title to show in a preview.

`image`

    

An image to show in a preview.

## See Also

### Displaying a preview with an image

`init(LocalizedStringKey, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

`init(Text, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

Initializer

# init(_:image:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: Image
    )

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

##  Parameters

`titleKey`

    

A key identifying a title to show in a preview.

`image`

    

An image to show in a preview.

## See Also

### Displaying a preview with an image

`init<S>(S, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

`init(Text, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

Initializer

# init(_:image:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        image: Image
    )

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

##  Parameters

`title`

    

A title to show in a preview.

`image`

    

An image to show in a preview.

## See Also

### Displaying a preview with an image

`init<S>(S, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

`init(LocalizedStringKey, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

Initializer

# init(_:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        icon: Icon
    ) where S : StringProtocol

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

##  Parameters

`title`

    

A title to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an icon

`init(LocalizedStringKey, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

`init(Text, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

Initializer

# init(_:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        icon: Icon
    )

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

##  Parameters

`titleKey`

    

A key identifying a title to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an icon

`init<S>(S, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

`init(Text, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

Initializer

# init(_:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        icon: Icon
    )

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

##  Parameters

`title`

    

A title to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an icon

`init<S>(S, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

`init(LocalizedStringKey, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

Initializer

# init(_:image:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: Image,
        icon: Icon
    ) where S : StringProtocol

##  Parameters

`title`

    

A title to show in a preview.

`image`

    

An image to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an image and an icon

`init(LocalizedStringKey, image: Image, icon: Icon)`

Creates a preview representation.

`init(Text, image: Image, icon: Icon)`

Creates a preview representation.

Initializer

# init(_:image:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: Image,
        icon: Icon
    )

##  Parameters

`titleKey`

    

A key identifying a title to show in a preview.

`image`

    

An image to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an image and an icon

`init<S>(S, image: Image, icon: Icon)`

Creates a preview representation.

`init(Text, image: Image, icon: Icon)`

Creates a preview representation.

Initializer

# init(_:image:icon:)

Creates a preview representation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        image: Image,
        icon: Icon
    )

##  Parameters

`title`

    

A title to show in a preview.

`image`

    

An image to show in a preview.

`icon`

    

An icon to show in a preview.

## See Also

### Displaying a preview with an image and an icon

`init<S>(S, image: Image, icon: Icon)`

Creates a preview representation.

`init(LocalizedStringKey, image: Image, icon: Icon)`

Creates a preview representation.

