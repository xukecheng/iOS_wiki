Case

# SnapshotData.SnapshotReason.appBackgrounded

The app transitioned from the foreground to the background.

watchOS 9.0+

    
    
    case appBackgrounded

## See Also

### Getting the snapshot reasons

`case appScheduled`

The app scheduled this snapshot.

`case complicationUpdate`

The app updated the complication timeline.

`case prelaunch`

The system needs a snapshot for the dock, but the app has not been launched
yet.

`case returnToDefaultState`

It has been more than an hour since the user’s last interaction with the app;
the app’s snapshot should return to its default state.

Case

# SnapshotData.SnapshotReason.appScheduled

The app scheduled this snapshot.

watchOS 9.0+

    
    
    case appScheduled

## See Also

### Getting the snapshot reasons

`case appBackgrounded`

The app transitioned from the foreground to the background.

`case complicationUpdate`

The app updated the complication timeline.

`case prelaunch`

The system needs a snapshot for the dock, but the app has not been launched
yet.

`case returnToDefaultState`

It has been more than an hour since the user’s last interaction with the app;
the app’s snapshot should return to its default state.

Case

# SnapshotData.SnapshotReason.complicationUpdate

The app updated the complication timeline.

watchOS 9.0+

    
    
    case complicationUpdate

## See Also

### Getting the snapshot reasons

`case appBackgrounded`

The app transitioned from the foreground to the background.

`case appScheduled`

The app scheduled this snapshot.

`case prelaunch`

The system needs a snapshot for the dock, but the app has not been launched
yet.

`case returnToDefaultState`

It has been more than an hour since the user’s last interaction with the app;
the app’s snapshot should return to its default state.

Case

# SnapshotData.SnapshotReason.prelaunch

The system needs a snapshot for the dock, but the app has not been launched
yet.

watchOS 9.0+

    
    
    case prelaunch

## See Also

### Getting the snapshot reasons

`case appBackgrounded`

The app transitioned from the foreground to the background.

`case appScheduled`

The app scheduled this snapshot.

`case complicationUpdate`

The app updated the complication timeline.

`case returnToDefaultState`

It has been more than an hour since the user’s last interaction with the app;
the app’s snapshot should return to its default state.

Case

# SnapshotData.SnapshotReason.returnToDefaultState

It has been more than an hour since the user’s last interaction with the app;
the app’s snapshot should return to its default state.

watchOS 9.0+

    
    
    case returnToDefaultState

## See Also

### Getting the snapshot reasons

`case appBackgrounded`

The app transitioned from the foreground to the background.

`case appScheduled`

The app scheduled this snapshot.

`case complicationUpdate`

The app updated the complication timeline.

`case prelaunch`

The system needs a snapshot for the dock, but the app has not been launched
yet.

