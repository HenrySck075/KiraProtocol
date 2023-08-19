
from . import _ok as base

class Network(base.sendhelp):

    method_ClearBrowserCache:str
    method_ClearBrowserCookies:str
    method_DeleteCookies:str
    method_Disable:str
    method_EmulateNetworkConditions:str
    method_Enable:str
    method_GetCookies:str
    method_GetRequestPostData:str
    method_GetResponseBody:str
    method_SetCacheDisabled:str
    method_SetCookie:str
    method_SetCookies:str
    method_SetExtraHTTPHeaders:str
    method_SetUserAgentOverride:str
    method_CanClearBrowserCache:str
    method_CanClearBrowserCookies:str
    method_CanEmulateNetworkConditions:str
    method_GetAllCookies:str
    method_ClearAcceptedEncodingsOverride:str
    method_EnableReportingApi:str
    method_GetCertificate:str
    method_GetResponseBodyForInterception:str
    method_GetSecurityIsolationStatus:str
    method_LoadNetworkResource:str
    method_ReplayXHR:str
    method_SearchInResponseBody:str
    method_SetAcceptedEncodings:str
    method_SetAttachDebugStack:str
    method_SetBlockedURLs:str
    method_SetBypassServiceWorker:str
    method_TakeResponseBodyForInterceptionAsStream:str
    method_ContinueInterceptedRequest:str
    method_SetRequestInterception:str

    event_DataReceived:str
    event_EventSourceMessageReceived:str
    event_LoadingFailed:str
    event_LoadingFinished:str
    event_RequestServedFromCache:str
    event_RequestWillBeSent:str
    event_ResponseReceived:str
    event_WebSocketClosed:str
    event_WebSocketCreated:str
    event_WebSocketFrameError:str
    event_WebSocketFrameReceived:str
    event_WebSocketFrameSent:str
    event_WebSocketHandshakeResponseReceived:str
    event_WebSocketWillSendHandshakeRequest:str
    event_WebTransportClosed:str
    event_WebTransportConnectionEstablished:str
    event_WebTransportCreated:str
    event_ReportingApiEndpointsChangedForOrigin:str
    event_ReportingApiReportAdded:str
    event_ReportingApiReportUpdated:str
    event_RequestWillBeSentExtraInfo:str
    event_ResourceChangedPriority:str
    event_ResponseReceivedExtraInfo:str
    event_SignedExchangeReceived:str
    event_SubresourceWebBundleInnerResponseError:str
    event_SubresourceWebBundleInnerResponseParsed:str
    event_SubresourceWebBundleMetadataError:str
    event_SubresourceWebBundleMetadataReceived:str
    event_TrustTokenOperationDone:str
    event_RequestIntercepted:str

    type_BlockedReason:str
    type_CachedResource:str
    type_CertificateTransparencyCompliance:str
    type_ConnectionType:str
    type_Cookie:str
    type_CookieParam:str
    type_CookieSameSite:str
    type_CorsError:str
    type_CorsErrorStatus:str
    type_ErrorReason:str
    type_Headers:str
    type_Initiator:str
    type_InterceptionId:str
    type_LoaderId:str
    type_MonotonicTime:str
    type_PostDataEntry:str
    type_Request:str
    type_RequestId:str
    type_ResourcePriority:str
    type_ResourceTiming:str
    type_ResourceType:str
    type_Response:str
    type_SecurityDetails:str
    type_ServiceWorkerResponseSource:str
    type_SignedCertificateTimestamp:str
    type_TimeSinceEpoch:str
    type_WebSocketFrame:str
    type_WebSocketRequest:str
    type_WebSocketResponse:str
    type_AlternateProtocolUsage:str
    type_AuthChallenge:str
    type_AuthChallengeResponse:str
    type_BlockedCookieWithReason:str
    type_BlockedSetCookieWithReason:str
    type_ClientSecurityState:str
    type_ConnectTiming:str
    type_ContentEncoding:str
    type_ContentSecurityPolicySource:str
    type_ContentSecurityPolicyStatus:str
    type_CookieBlockedReason:str
    type_CookiePriority:str
    type_CookieSourceScheme:str
    type_CrossOriginEmbedderPolicyStatus:str
    type_CrossOriginEmbedderPolicyValue:str
    type_CrossOriginOpenerPolicyStatus:str
    type_CrossOriginOpenerPolicyValue:str
    type_InterceptionStage:str
    type_IPAddressSpace:str
    type_LoadNetworkResourceOptions:str
    type_LoadNetworkResourcePageResult:str
    type_PrivateNetworkRequestPolicy:str
    type_ReportId:str
    type_ReportingApiEndpoint:str
    type_ReportingApiReport:str
    type_ReportStatus:str
    type_RequestPattern:str
    type_SecurityIsolationStatus:str
    type_SetCookieBlockedReason:str
    type_SignedExchangeError:str
    type_SignedExchangeErrorField:str
    type_SignedExchangeHeader:str
    type_SignedExchangeInfo:str
    type_SignedExchangeSignature:str
    type_TrustTokenOperationType:str
    type_TrustTokenParams:str

    def __init__(self):
        super().__init__()

    
domain = Network()