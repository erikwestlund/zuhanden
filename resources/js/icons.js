import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faBars,
    faChevronRight,
    faChevronDown,
    faCircleNotch,
    faCloudUpload,
    faCopy,
    faCut,
    faEdit,
    faEllipsisH,
    faEnvelope,
    faExclamationCircle,
    faExternalLink,
    faEye,
    faEyeSlash,
    faFileAlt,
    faFileEdit,
    faImages,
    faKey,
    faLink,
    faList,
    faLock,
    faPencil,
    faPlusCircle,
    faPlusSquare,
    faSave,
    faSearch,
    faSignIn,
    faSignOut,
    faTag,
    faTags,
    faTimes,
    faTrash,
    faUniversity,
    faUpload,
    faUser,
    faUserCircle,
    faUserEdit,
    faUserPlus,
    faWindowRestore
} from '@fortawesome/pro-regular-svg-icons'

import {
    faEnvelope as fasEnvelope,
    faHammer as fasHammer,
    faSignIn as fasSignIn,
    faSignOut as fasSignOut,
    faUserCircle as fasUserCircle,
    faUserPlus as fasUserPlus,
    faUniversity as fasUniversity
} from '@fortawesome/pro-solid-svg-icons'

import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faBars,
    faChevronRight,
    faChevronDown,
    faCircleNotch,
    faCloudUpload,
    faCut,
    faCopy,
    faEdit,
    faEllipsisH,
    faEnvelope,
    fasEnvelope,
    faExclamationCircle,
    faExternalLink,
    faEye,
    faEyeSlash,
    faFileAlt,
    faGithub,
    faFileEdit,
    fasHammer,
    faImages,
    faKey,
    faLink,
    faList,
    faLock,
    faPencil,
    faPlusCircle,
    faPlusSquare,
    faSave,
    faSearch,
    faSignIn,
    faSignOut,
    fasSignIn,
    fasSignOut,
    faTag,
    faTags,
    faTimes,
    faTrash,
    faTwitter,
    faUpload,
    faUser,
    faUserCircle,
    fasUserCircle,
    faUserEdit,
    faUserPlus,
    fasUserPlus,
    faUniversity,
    fasUniversity,
    faWindowRestore
)

Vue.component('fa-icon', FontAwesomeIcon)
Vue.component('fa-layers', FontAwesomeLayers)
