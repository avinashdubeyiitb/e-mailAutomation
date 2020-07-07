import Vue from 'vue'
import Vuex from 'vuex'
import statedisdata from '../assets/states-and-districts.json'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      token: null,
      success: false,
      url: 'http://localhost:8081',
      user_name: '',
      csvapp: false, // sim
      csvgsave: false,
      simisNight: true,
      simisNight1: true,
      simisNight2: true,
      simisNight3: true,
      iscsvtrue: false,
      statedisdata: statedisdata,
      state: 'State',
      index: '',
      in: '',
      value: '',
      districts: [],
      d: 'District',
      district: [],
      remail: '',
      cc: '',
      bcc: '',
      name: '',
      designation: '',
      department: '',
      cname: '',
      cno: '',
      output: '',
      items: [],
      selected: [],
      selectAll: false,
      file: '',
      upfile1: [],
      upfile2: [],
      reqdata: '',
      approvecsv: '',
      gsavecsv: '',
      aprovselected: [],
      gsvselected: [],
      dscrdselected: [],
      detail: [],
      mulupfile1: [],
      mulupfile2: [],
      cwsstate: 'State', // cws
      cwsindex: '',
      startdate: '',
      enddate: '',
      venueadd: '',
      cooname: '',
      cooemail: '',
      coono: '',
      cwsoutput: '',
      selectedhcn: '',
      hcn: [],
      cwssuccess: false,
      showing: 'false',
      awsstate: 'State', // aws
      awsindex: '',
      awsin: '',
      awswrklist: [],
      awsshowing: 'false',
      awsdistricts: [],
      awsd: 'District',
      awsdistrict: [],
      awsisNight: true,
      awsisNight1: true,
      awsisNight2: true,
      awsisNight3: true,
      awsselectedworkshop: '',
      awshcn: '',
      filldate: '',
      awsoutput: '',
      awsitems: [],
      awsselected: [],
      awsselectAll: false,
      awsreqdata: '',
      awseditedTodo: null,
      awsupfile1: [],
      awsupfile2: '',
      result: '',
      selectedworkshop: '',
      wrklist: [],
      lang: [],
      algoshowing: 'false',
      selectedlang: '',
      algooutput: ''
    }
  },
  getters: {
    token: state => {
      return state.user.token
    }, // sim
    success: state => {
      return state.user.success
    },
    url: state => {
      return state.user.url
    },
    user_name: state => {
      return state.user.user_name
    },
    csvapp: state => {
      return state.user.csvapp
    }, // sim
    csvgsave: state => {
      return state.user.csvgsave
    },
    simisNight: state => {
      return state.user.simisNight
    },
    simisNight1: state => {
      return state.user.simisNight1
    },
    simisNight2: state => {
      return state.user.simisNight2
    },
    simisNight3: state => {
      return state.user.simisNight3
    },
    iscsvtrue: state => {
      return state.user.iscsvtrue
    },
    statedisdata: state => {
      return state.user.statedisdata
    },
    state: state => {
      return state.user.state
    },
    index: state => {
      return state.user.index
    },
    in: state => {
      return state.user.in
    },
    value: state => {
      return state.user.value
    },
    districts: state => {
      return state.user.districts
    },
    d: state => {
      return state.user.d
    },
    district: state => {
      return state.user.district
    },
    remail: state => {
      return state.user.remail
    },
    cc: state => {
      return state.user.cc
    },
    bcc: state => {
      return state.user.bcc
    },
    name: state => {
      return state.user.name
    },
    designation: state => {
      return state.user.designation
    },
    department: state => {
      return state.user.department
    },
    cname: state => {
      return state.user.cname
    },
    cno: state => {
      return state.user.cno
    },
    output: state => {
      return state.user.output
    },
    items: state => {
      return state.user.items
    },
    selected: state => {
      return state.user.selected
    },
    selectAll: state => {
      return state.user.selectAll
    },
    file: state => {
      return state.user.file
    },
    upfile1: state => {
      return state.user.upfile1
    },
    upfile2: state => {
      return state.user.upfile2
    },
    reqdata: state => {
      return state.user.reqdata
    },
    approvecsv: state => {
      return state.user.approvecsv
    },
    gsavecsv: state => {
      return state.user.gsavecsv
    },
    aprovselected: state => {
      return state.user.aprovselected
    },
    gsvselected: state => {
      return state.user.gsvselected
    },
    dscrdselected: state => {
      return state.user.dscrdselected
    },
    detail: state => {
      return state.user.detail
    },
    mulupfile1: state => {
      return state.user.mulupfile1
    },
    mulupfile2: state => {
      return state.user.mulupfile2
    },
    cwsstate: state => {
      return state.user.cwsstate
    }, // cws
    cwsindex: state => {
      return state.user.cwsindex
    },
    startdate: state => {
      return state.user.startdate
    },
    enddate: state => {
      return state.user.enddate
    },
    venueadd: state => {
      return state.user.venueadd
    },
    cooname: state => {
      return state.user.cooname
    },
    cooemail: state => {
      return state.user.cooemail
    },
    coono: state => {
      return state.user.coono
    },
    cwsoutput: state => {
      return state.user.cwsoutput
    },
    selectedhcn: state => {
      return state.user.selectedhcn
    },
    hcn: state => {
      return state.user.hcn
    },
    cwssuccess: state => {
      return state.user.success
    },
    showing: state => {
      return state.user.showing
    },
    awsstate: state => {
      return state.user.awsstate
    }, // aws
    awsindex: state => {
      return state.user.awsindex
    },
    awsin: state => {
      return state.user.awsin
    },
    awswrklist: state => {
      return state.user.awswrklist
    },
    awsshowing: state => {
      return state.user.awsshowing
    },
    awsdistricts: state => {
      return state.user.awsdistricts
    },
    awsd: state => {
      return state.user.awsd
    },
    awsdistrict: state => {
      return state.user.awsdistrict
    },
    awsisNight: state => {
      return state.user.awsisNight
    },
    awsisNight1: state => {
      return state.user.awsisNight1
    },
    awsisNight2: state => {
      return state.user.awsisNight2
    },
    awsisNight3: state => {
      return state.user.awsisNight3
    },
    awsselectedworkshop: state => {
      return state.user.awsselectedworkshop
    },
    awshcn: state => {
      return state.user.awshcn
    },
    filldate: state => {
      return state.user.filldate
    },
    awsoutput: state => {
      return state.user.awsoutput
    },
    awsitems: state => {
      return state.user.awsitems
    },
    awsselected: state => {
      return state.user.awsselected
    },
    awsselectAll: state => {
      return state.user.awsselectAll
    },
    awsreqdata: state => {
      return state.user.awsreqdata
    },
    awseditedTodo: state => {
      return state.user.awseditedTodo
    },
    awsupfile1: state => {
      return state.user.awsupfile1
    },
    awsupfile2: state => {
      return state.user.awsupfile2
    },
    result: state => {
      return state.user.result
    },
    selectedworkshop: state => {
      return state.user.selectedworkshop
    },
    wrklist: state => {
      return state.user.wrklist
    },
    lang: state => {
      return state.user.lang
    },
    algoshowing: state => {
      return state.user.algoshowing
    },
    selectedlang: state => {
      return state.user.selectedlang
    },
    algooutput: state => {
      return state.user.algooutput
    }
  },
  mutations: {
    token (state, payload) {
      state.user.token = payload
    },
    success (state, payload) {
      state.user.success = payload
    },
    url (state, payload) {
      state.user.url = payload
    },
    user_name (state, payload) {
      state.user.user_name = payload
    },
    csvapp (state, payload) {
      state.user.csvapp = payload
    }, // sim
    csvgsave (state, payload) {
      state.user.csvgsave = payload
    },
    simisNight (state, payload) {
      state.user.simisNight = payload
    },
    simisNight1 (state, payload) {
      state.user.simisNight1 = payload
    },
    simisNight2 (state, payload) {
      state.user.simisNight2 = payload
    },
    simisNight3 (state, payload) {
      state.user.simisNight3 = payload
    },
    iscsvtrue (state, payload) {
      state.user.iscsvtrue = payload
    },
    state (state, payload) {
      state.user.state = payload
    },
    index (state, payload) {
      state.user.index = payload
    },
    in (state, payload) {
      state.user.in = payload
    },
    value (state, payload) {
      state.user.value = payload
    },
    districts (state, payload) {
      state.user.districts = payload
    },
    d (state, payload) {
      state.user.d = payload
    },
    district (state, payload) {
      state.user.district = payload
    },
    remail (state, payload) {
      state.user.remail = payload
    },
    cc (state, payload) {
      state.user.cc = payload
    },
    bcc (state, payload) {
      state.user.bcc = payload
    },
    name (state, payload) {
      state.user.name = payload
    },
    designation (state, payload) {
      state.user.designation = payload
    },
    department (state, payload) {
      state.user.department = payload
    },
    cname (state, payload) {
      state.user.cname = payload
    },
    cno (state, payload) {
      state.user.cno = payload
    },
    output (state, payload) {
      state.user.output = payload
    },
    items (state, payload) {
      state.user.items = payload
    },
    selected (state, payload) {
      state.user.selected = payload
    },
    selectAll (state, payload) {
      state.user.selectAll = payload
    },
    file (state, payload) {
      state.user.file = payload
    },
    upfile1 (state, payload) {
      state.user.upfile1 = payload
    },
    upfile2 (state, payload) {
      state.user.upfile2 = payload
    },
    reqdata (state, payload) {
      state.user.reqdata = payload
    },
    approvecsv (state, payload) {
      state.user.approvecsv = payload
    },
    gsavecsv (state, payload) {
      state.user.gsavecsv = payload
    },
    aprovselected (state, payload) {
      state.user.aprovselected = payload
    },
    gsvselected (state, payload) {
      state.user.gsvselected = payload
    },
    dscrdselected (state, payload) {
      state.user.dscrdselected = payload
    },
    detail (state, payload) {
      state.user.detail = payload
    },
    mulupfile1 (state, payload) {
      state.user.mulupfile1 = payload
    },
    mulupfile2 (state, payload) {
      state.user.mulupfile2 = payload
    },
    cwsstate (state, payload) {
      state.user.cwsstate = payload
    }, // cws
    cwsindex (state, payload) {
      state.user.cwsindex = payload
    },
    startdate (state, payload) {
      state.user.startdate = payload
    },
    enddate (state, payload) {
      state.user.enddate = payload
    },
    venueadd (state, payload) {
      state.user.venueadd = payload
    },
    cooname (state, payload) {
      state.user.cooname = payload
    },
    cooemail (state, payload) {
      state.user.cooemail = payload
    },
    coono (state, payload) {
      state.user.coono = payload
    },
    cwsoutput (state, payload) {
      state.user.cwsoutput = payload
    },
    selectedhcn (state, payload) {
      state.user.selectedhcn = payload
    },
    hcn (state, payload) {
      state.user.hcn = payload
    },
    cwssuccess (state, payload) {
      state.user.success = payload
    },
    showing (state, payload) {
      state.user.showing = payload
    },
    awsstate (state, payload) {
      state.user.awsstate = payload
    }, // aws
    awsindex (state, payload) {
      state.user.awsindex = payload
    },
    awsin (state, payload) {
      state.user.awsin = payload
    },
    awswrklist (state, payload) {
      state.user.awswrklist = payload
    },
    awsshowing (state, payload) {
      state.user.awsshowing = payload
    },
    awsdistricts (state, payload) {
      state.user.awsdistricts = payload
    },
    awsd (state, payload) {
      state.user.awsd = payload
    },
    awsdistrict (state, payload) {
      state.user.awsdistrict = payload
    },
    awsisNight (state, payload) {
      state.user.awsisNight = payload
    },
    awsisNight1 (state, payload) {
      state.user.awsisNight1 = payload
    },
    awsisNight2 (state, payload) {
      state.user.awsisNight2 = payload
    },
    awsisNight3 (state, payload) {
      state.user.awsisNight3 = payload
    },
    awsselectedworkshop (state, payload) {
      state.user.awsselectedworkshop = payload
    },
    awshcn (state, payload) {
      state.user.awshcn = payload
    },
    filldate (state, payload) {
      state.user.filldate = payload
    },
    awsoutput (state, payload) {
      state.user.awsoutput = payload
    },
    awsitems (state, payload) {
      state.user.awsitems = payload
    },
    awsselected (state, payload) {
      state.user.awsselected = payload
    },
    awsselectAll (state, payload) {
      state.user.awsselectAll = payload
    },
    awsreqdata (state, payload) {
      state.user.awsreqdata = payload
    },
    awseditedTodo (state, payload) {
      state.user.awseditedTodo = payload
    },
    awsupfile1 (state, payload) {
      state.user.awsupfile1 = payload
    },
    awsupfile2 (state, payload) {
      state.user.awsupfile2 = payload
    },
    result (state, payload) {
      state.user.result = payload
    },
    selectedworkshop (state, payload) {
      state.user.selectedworkshop = payload
    },
    wrklist (state, payload) {
      state.user.wrklist = payload
    },
    lang (state, payload) {
      state.user.lang = payload
    },
    algoshowing (state, payload) {
      state.user.algoshowing = payload
    },
    selectedlang (state, payload) {
      state.user.selectedlang = payload
    },
    algooutput (state, payload) {
      state.user.algooutput = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
