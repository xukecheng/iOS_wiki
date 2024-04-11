Type Property

# characters

Defines an autocapitalizing behavior that will capitalize every letter.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var characters: TextInputAutocapitalization { get }

## See Also

### Getting autocapitalization options

`static var sentences: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter in
every sentence.

`static var words: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter of
every word.

`static var never: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will not capitalize anything.

Type Property

# sentences

Defines an autocapitalizing behavior that will capitalize the first letter in
every sentence.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var sentences: TextInputAutocapitalization { get }

## See Also

### Getting autocapitalization options

`static var characters: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize every letter.

`static var words: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter of
every word.

`static var never: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will not capitalize anything.

Type Property

# words

Defines an autocapitalizing behavior that will capitalize the first letter of
every word.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var words: TextInputAutocapitalization { get }

## See Also

### Getting autocapitalization options

`static var characters: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize every letter.

`static var sentences: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter in
every sentence.

`static var never: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will not capitalize anything.

Type Property

# never

Defines an autocapitalizing behavior that will not capitalize anything.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var never: TextInputAutocapitalization { get }

## See Also

### Getting autocapitalization options

`static var characters: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize every letter.

`static var sentences: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter in
every sentence.

`static var words: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter of
every word.

Initializer

# init(_:)

Creates a new `TextInputAutocapitalization` struct from a
`UITextAutocapitalizationType` enum.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  visionOS 1.0+

    
    
    init?(_ type: UITextAutocapitalizationType)

