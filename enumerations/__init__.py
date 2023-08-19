__import__("os").environ["PYTHONDONTWRITEBYTECODE"] = "1"
from .accessibility import domain as Accessibility
from .animation import domain as Animation
from .audits import domain as Audits
from .autofill import domain as Autofill
from .backgroundservice import domain as BackgroundService
from .browser import domain as Browser
from .cachestorage import domain as CacheStorage
from .cast import domain as Cast
from .console import domain as Console
from .css import domain as CSS
from .database import domain as Database
from .debugger import domain as Debugger
from .deviceaccess import domain as DeviceAccess
from .deviceorientation import domain as DeviceOrientation
from .dom import domain as DOM
from .domdebugger import domain as DOMDebugger
from .domsnapshot import domain as DOMSnapshot
from .domstorage import domain as DOMStorage
from .emulation import domain as Emulation
from .eventbreakpoints import domain as EventBreakpoints
from .fedcm import domain as FedCm
from .fetch import domain as Fetch
from .headlessexperimental import domain as HeadlessExperimental
from .heapprofiler import domain as HeapProfiler
from .indexeddb import domain as IndexedDB
from .input import domain as Input
from .inspector import domain as Inspector
from .io import domain as IO
from .layertree import domain as LayerTree
from .log import domain as Log
from .media import domain as Media
from .memory import domain as Memory
from .network import domain as Network
from .overlay import domain as Overlay
from .page import domain as Page
from .performance import domain as Performance
from .performancetimeline import domain as PerformanceTimeline
from .preload import domain as Preload
from .profiler import domain as Profiler
from .runtime import domain as Runtime
from .schema import domain as Schema
from .security import domain as Security
from .serviceworker import domain as ServiceWorker
from .storage import domain as Storage
from .systeminfo import domain as SystemInfo
from .target import domain as Target
from .tethering import domain as Tethering
from .tracing import domain as Tracing
from .webaudio import domain as WebAudio
from .webauthn import domain as WebAuthn