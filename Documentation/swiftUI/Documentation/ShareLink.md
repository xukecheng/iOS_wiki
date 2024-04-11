Initializer

# init(item:subject:message:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        item: String,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<String>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing an item

`init(item: URL, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: String, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(item:subject:message:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        item: URL,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<URL>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing an item

`init(item: String, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: String, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(item:subject:message:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        item: String,
        subject: Text? = nil,
        message: Text? = nil,
        @ViewBuilder label: () -> Label
    ) where Data == CollectionOfOne<String>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing an item

`init(item: String, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(item:subject:message:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        item: URL,
        subject: Text? = nil,
        message: Text? = nil,
        @ViewBuilder label: () -> Label
    ) where Data == CollectionOfOne<URL>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing an item

`init(item: String, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: String, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(item:subject:message:preview:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<I>(
        item: I,
        subject: Text? = nil,
        message: Text? = nil,
        preview: SharePreview<PreviewImage, PreviewIcon>
    ) where Data == CollectionOfOne<I>, I : Transferable

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A representation of the item to render in a preview.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing an item with a preview

`init<I>(item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
conforms to `View`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(item:subject:message:preview:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<I>(
        item: I,
        subject: Text? = nil,
        message: Text? = nil,
        preview: SharePreview<PreviewImage, PreviewIcon>,
        @ViewBuilder label: () -> Label
    ) where Data == CollectionOfOne<I>, I : Transferable

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
conforms to `View`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A representation of the item to render in a preview.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing an item with a preview

`init<I>(item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        item: URL,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<URL>, S : StringProtocol

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        item: URL,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<URL>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        item: String,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<String>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        item: String,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<String>, S : StringProtocol

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        item: String,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<String>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        item: URL,
        subject: Text? = nil,
        message: Text? = nil
    ) where Data == CollectionOfOne<URL>

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S, I>(
        _ title: S,
        item: I,
        subject: Text? = nil,
        message: Text? = nil,
        preview: SharePreview<PreviewImage, PreviewIcon>
    ) where Data == CollectionOfOne<I>, S : StringProtocol, I : Transferable

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A representation of the item to render in a preview.

## See Also

### Sharing an item with a label and a preview

`init<I>(Text, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(LocalizedStringKey, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<I>(
        _ title: Text,
        item: I,
        subject: Text? = nil,
        message: Text? = nil,
        preview: SharePreview<PreviewImage, PreviewIcon>
    ) where Data == CollectionOfOne<I>, I : Transferable

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A representation of the item to render in a preview.

## See Also

### Sharing an item with a label and a preview

`init<S, I>(S, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(LocalizedStringKey, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:item:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<I>(
        _ titleKey: LocalizedStringKey,
        item: I,
        subject: Text? = nil,
        message: Text? = nil,
        preview: SharePreview<PreviewImage, PreviewIcon>
    ) where Data == CollectionOfOne<I>, I : Transferable

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`item`

    

The item to share.

`subject`

    

A title for the item to show when sharing to activities that support a subject
field.

`message`

    

A description of the item to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A representation of the item to render in a preview.

## See Also

### Sharing an item with a label and a preview

`init<S, I>(S, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(Text, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(items:subject:message:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing items

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `URL`.

Initializer

# init(items:subject:message:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing items

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `URL`.

Initializer

# init(items:subject:message:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        @ViewBuilder label: () -> Label
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `String`.

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing items

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `URL`.

Initializer

# init(items:subject:message:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        @ViewBuilder label: () -> Label
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `URL`.

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing items

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `String`.

Initializer

# init(items:subject:message:preview:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A closure that returns a representation of each item to render in a preview.

## Discussion

Use this initializer when you want the system-standard appearance for
`ShareLink`.

## See Also

### Sharing items with a preview

`init(items: Data, subject: Text?, message: Text?, preview: (Data.Element) ->
SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)`

Creates an instance that presents the share interface.

Initializer

# init(items:subject:message:preview:label:)

Creates an instance that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A closure that returns a representation of each item to render in a preview.

`label`

    

A view builder that produces a label that describes the share action.

## See Also

### Sharing items with a preview

`init(items: Data, subject: Text?, message: Text?, preview: (Data.Element) ->
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    ) where S : StringProtocol

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The item to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    ) where S : StringProtocol

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The item to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

Initializer

# init(_:items:subject:message:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

## See Also

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

Initializer

# init(_:items:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>
    ) where S : StringProtocol

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The item to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A closure that returns a representation of each item to render in a preview.

## See Also

### Sharing items with a label and preview

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?,
preview: (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(Text, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:items:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`titleKey`

    

A key identifying the title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A closure that returns a representation of each item to render in a preview.

## See Also

### Sharing items with a label and preview

`init<S>(S, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(Text, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Initializer

# init(_:items:subject:message:preview:)

Creates an instance, with a custom label, that presents the share interface.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ title: Text,
        items: Data,
        subject: Text? = nil,
        message: Text? = nil,
        preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>
    )

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

##  Parameters

`title`

    

The title of the share action.

`items`

    

The items to share.

`subject`

    

A title for the items to show when sharing to activities that support a
subject field.

`message`

    

A description of the items to show when sharing to activities that support a
message field. Activities may support attributed text or HTML strings.

`preview`

    

A closure that returns a representation of each item to render in a preview.

## See Also

### Sharing items with a label and preview

`init<S>(S, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?,
preview: (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

Structure

# DefaultShareLinkLabel

The default label used for a share link.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct DefaultShareLinkLabel

## Overview

You don’t use this type directly. Instead, `ShareLink` uses it automatically
depending on how you create a share link.

## Relationships

### Conforms To

  * `View`

