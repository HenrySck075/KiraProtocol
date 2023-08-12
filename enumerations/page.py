from . import _ok as base

class Page(base.sendhelp):

    method_AddScriptToEvaluateOnNewDocument:str
    method_BringToFront:str
    method_CaptureScreenshot:str
    method_CreateIsolatedWorld:str
    method_Disable:str
    method_Enable:str
    method_GetAppManifest:str
    method_GetFrameTree:str
    method_GetLayoutMetrics:str
    method_GetNavigationHistory:str
    method_HandleJavaScriptDialog:str
    method_Navigate:str
    method_NavigateToHistoryEntry:str
    method_PrintToPDF:str
    method_Reload:str
    method_RemoveScriptToEvaluateOnNewDocument:str
    method_ResetNavigationHistory:str
    method_SetDocumentContent:str
    method_StopLoading:str
    method_ClearGeolocationOverride:str
    method_SetGeolocationOverride:str
    method_AddCompilationCache:str
    method_CaptureSnapshot:str
    method_ClearCompilationCache:str
    method_Close:str
    method_Crash:str
    method_GenerateTestReport:str
    method_GetAdScriptId:str
    method_GetAppId:str
    method_GetInstallabilityErrors:str
    method_GetOriginTrials:str
    method_GetPermissionsPolicyState:str
    method_GetResourceContent:str
    method_GetResourceTree:str
    method_ProduceCompilationCache:str
    method_ScreencastFrameAck:str
    method_SearchInResource:str
    method_SetAdBlockingEnabled:str
    method_SetBypassCSP:str
    method_SetFontFamilies:str
    method_SetFontSizes:str
    method_SetInterceptFileChooserDialog:str
    method_SetLifecycleEventsEnabled:str
    method_SetPrerenderingAllowed:str
    method_SetRPHRegistrationMode:str
    method_SetSPCTransactionMode:str
    method_SetWebLifecycleState:str
    method_StartScreencast:str
    method_StopScreencast:str
    method_WaitForDebugger:str
    method_AddScriptToEvaluateOnLoad:str
    method_ClearDeviceMetricsOverride:str
    method_ClearDeviceOrientationOverride:str
    method_DeleteCookie:str
    method_GetCookies:str
    method_GetManifestIcons:str
    method_RemoveScriptToEvaluateOnLoad:str
    method_SetDeviceMetricsOverride:str
    method_SetDeviceOrientationOverride:str
    method_SetDownloadBehavior:str
    method_SetTouchEmulationEnabled:str

    event_DomContentEventFired:str
    event_FileChooserOpened:str
    event_FrameAttached:str
    event_FrameDetached:str
    event_FrameNavigated:str
    event_InterstitialHidden:str
    event_InterstitialShown:str
    event_JavascriptDialogClosed:str
    event_JavascriptDialogOpening:str
    event_LifecycleEvent:str
    event_LoadEventFired:str
    event_WindowOpen:str
    event_FrameClearedScheduledNavigation:str
    event_FrameScheduledNavigation:str
    event_BackForwardCacheNotUsed:str
    event_CompilationCacheProduced:str
    event_DocumentOpened:str
    event_FrameRequestedNavigation:str
    event_FrameResized:str
    event_FrameStartedLoading:str
    event_FrameStoppedLoading:str
    event_NavigatedWithinDocument:str
    event_ScreencastFrame:str
    event_ScreencastVisibilityChanged:str
    event_DownloadProgress:str
    event_DownloadWillBegin:str

    type_AppManifestError:str
    type_DialogType:str
    type_Frame:str
    type_FrameId:str
    type_FrameTree:str
    type_LayoutViewport:str
    type_NavigationEntry:str
    type_ScriptIdentifier:str
    type_TransitionType:str
    type_Viewport:str
    type_VisualViewport:str
    type_AdFrameExplanation:str
    type_AdFrameStatus:str
    type_AdFrameType:str
    type_AdScriptId:str
    type_AppManifestParsedProperties:str
    type_AutoResponseMode:str
    type_BackForwardCacheNotRestoredExplanation:str
    type_BackForwardCacheNotRestoredExplanationTree:str
    type_BackForwardCacheNotRestoredReason:str
    type_BackForwardCacheNotRestoredReasonType:str
    type_ClientNavigationDisposition:str
    type_ClientNavigationReason:str
    type_CompilationCacheParams:str
    type_CrossOriginIsolatedContextType:str
    type_FontFamilies:str
    type_FontSizes:str
    type_FrameResource:str
    type_FrameResourceTree:str
    type_GatedAPIFeatures:str
    type_InstallabilityError:str
    type_InstallabilityErrorArgument:str
    type_NavigationType:str
    type_OriginTrial:str
    type_OriginTrialStatus:str
    type_OriginTrialToken:str
    type_OriginTrialTokenStatus:str
    type_OriginTrialTokenWithStatus:str
    type_OriginTrialUsageRestriction:str
    type_PermissionsPolicyBlockLocator:str
    type_PermissionsPolicyBlockReason:str
    type_PermissionsPolicyFeature:str
    type_PermissionsPolicyFeatureState:str
    type_ReferrerPolicy:str
    type_ScreencastFrameMetadata:str
    type_ScriptFontFamilies:str
    type_SecureContextType:str

    def __init__(self):
        super().__init__()

    
domain = Page()