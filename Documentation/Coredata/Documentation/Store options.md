Global Variable

# NSReadOnlyPersistentStoreOption

A flag that indicates whether a store is treated as read-only or not.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSReadOnlyPersistentStoreOption: String

## Discussion

The default value is `false`.

Global Variable

# NSValidateXMLStoreOption

A flag that indicates whether an XML file should be validated with the DTD
while opening.

macOS 10.4+

    
    
    let NSValidateXMLStoreOption: String

## Discussion

The default value is `false`.

Global Variable

# NSPersistentStoreTimeoutOption

Options key that specifies the connection timeout for Core Data stores.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSPersistentStoreTimeoutOption: String

## Discussion

The corresponding value is an `NSNumber` object that represents the duration
in seconds that Core Data will wait while attempting to create a connection to
a persistent store. If a connection is cannot be made within that timeframe,
the operation is aborted and an error is returned.

Global Variable

# NSSQLitePragmasOption

Options key for a dictionary of SQLite pragma settings with pragma values
indexed by pragma names as keys.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSSQLitePragmasOption: String

## Discussion

All pragma values must be specified as `NSString` objects. The `fullfsync` and
`synchronous` pragmas control the tradeoff between write performance (write to
disk speed & cache utilization) and durability (data loss/corruption
sensitivity to power interruption). For more information on pragma settings,
see http://sqlite.org/pragma.html.

Global Variable

# NSSQLiteAnalyzeOption

Option key to run an analysis of the store data to optimize indices based on
statistical information when the store is added to the coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSSQLiteAnalyzeOption: String

## Discussion

This invokes SQLite's `ANALYZE` command. It is ignored by stores other than
the SQLite store.

Global Variable

# NSSQLiteManualVacuumOption

Option key to rebuild the store file, forcing a database wide defragmentation
when the store is added to the coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSSQLiteManualVacuumOption: String

## Discussion

This invokes SQLite's `VACUUM` command. It is ignored by stores other than the
SQLite store.

Global Variable

# NSPersistentStoreFileProtectionKey

Key to represent the protection class for the persistent store.

iOS 5.0+  iPadOS 5.0+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS 2.0+  visionOS
1.0+

    
    
    let NSPersistentStoreFileProtectionKey: String

## Discussion

Backward compatibility may preclude some features. The acceptable values are
those defined for the `protectionKey`. The default value is
`completeUntilFirstUserAuthentication` for all applications built on or after
iOS v5.0. The default value for all older applications is `none`.

Global Variable

# NSPersistentStoreForceDestroyOption

A flag that indicates the coordinator destroys the store file even if the
operation might be unsafe, overriding locks, if necessary.

iOS 6.0+  iPadOS 6.0+  macOS 10.8+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSPersistentStoreForceDestroyOption: String

Global Variable

# NSExternalRecordsDirectoryOption

Option indicating the directory where Spotlight external record files should
be written to.

macOS 10.6–10.13  Deprecated

    
    
    let NSExternalRecordsDirectoryOption: String

## See Also

### Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSExternalRecordExtensionOption

Option indicating the file extension to use for Spotlight external record
files.

macOS 10.6–10.13  Deprecated

    
    
    let NSExternalRecordExtensionOption: String

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSExternalRecordsFileFormatOption

Option to specify the file format of a Spotlight external records.

macOS 10.6–10.13  Deprecated

    
    
    let NSExternalRecordsFileFormatOption: String

## Discussion

For possible values, see `Format Options for Spotlight External Record Files`.

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreUbiquitousContentNameKey

Option to specify that a persistent store has a given name in ubiquity.

iOS 5.0–10.0  Deprecated  iPadOS 5.0–10.0  Deprecated  macOS 10.7–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreUbiquitousContentNameKey: String

## Discussion

This option is required for ubiquitous content to function.

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreUbiquitousContentURLKey

Option to specify the log path to use for ubiquitous content logs.

iOS 5.0–10.0  Deprecated  iPadOS 5.0–10.0  Deprecated  macOS 10.7–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreUbiquitousContentURLKey: String

## Discussion

In iOS 6 and OS X 10.8 and below, this option is required for ubiquitous
content to function. In iOS 7 and macOS 10.9 and later, it is optional.

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreUbiquitousPeerTokenOption

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreUbiquitousPeerTokenOption: String

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreRemoveUbiquitousMetadataOption

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreRemoveUbiquitousMetadataOption: String

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreUbiquitousContainerIdentifierKey

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreUbiquitousContainerIdentifierKey: String

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreRebuildFromUbiquitousContentOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

Deprecated

Global Variable

# NSPersistentStoreRebuildFromUbiquitousContentOption

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should erase the local store file and rebuild
it from the iCloud data in Mobile Documents.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    let NSPersistentStoreRebuildFromUbiquitousContentOption: String

## See Also

### Deprecated

`let NSExternalRecordsDirectoryOption: String`

Option indicating the directory where Spotlight external record files should
be written to.

Deprecated

`let NSExternalRecordExtensionOption: String`

Option indicating the file extension to use for Spotlight external record
files.

Deprecated

`let NSExternalRecordsFileFormatOption: String`

Option to specify the file format of a Spotlight external records.

Deprecated

`let NSPersistentStoreUbiquitousContentNameKey: String`

Option to specify that a persistent store has a given name in ubiquity.

Deprecated

`let NSPersistentStoreUbiquitousContentURLKey: String`

Option to specify the log path to use for ubiquitous content logs.

Deprecated

`let NSPersistentStoreUbiquitousPeerTokenOption: String`

The corresponding value is an optionally specified string which will be mixed
in to Core Data’s identifier for each iCloud peer. The value must be an
alphanumeric string without any special characters, whitespace or punctuation.
The primary use for this option is to allow multiple applications on the same
peer (device) to share a Core Data store integrated with iCloud. Each
application will require its own store file.

Deprecated

`let NSPersistentStoreRemoveUbiquitousMetadataOption: String`

The corresponding value is an `NSNumber` object representing a boolean that
indicates whether the receiver should remove all associated ubiquity metadata
from a persistent store. You typically use this option during migration or
copying to disassociate a persistent store file from an iCloud account.

Deprecated

`let NSPersistentStoreUbiquitousContainerIdentifierKey: String`

The corresponding value is a string specifying the iCloud container identifier
Core Data should pass to `url(forUbiquityContainerIdentifier:)`.

Deprecated

